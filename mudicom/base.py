# -*- coding: utf-8 -*-
"""
    mudicom.base
    ~~~~~~~~~~~~

    Primary functionality for reading DICOM files using the Dicom and
    DataElement class definitions.
"""
import os
import json
import gdcm

from .validation import validate
from .image import Image
from .exceptions import InvalidDicom

def get_anon_tags():
    BASE_DIR = os.path.dirname(os.path.realpath(__file__))
    data = None
    with open(os.path.join(BASE_DIR, "json/deidentify.json"), "r") as fp:
        data = json.load(fp)
    return data


class DataElement(object):
    """ Object representation of a Data Element

    :param swig_element: GDCMs DataElement SWIG object
    :param name: Name of DICOM data element
    :param value: Value of DICOM data element

    * DataElement Properties:
        * name: Name of DICOM data element
        * Value: Value of data element
        * VR: Value Representation of data element
        * VL: Value Length of data element
        * tag: Dictionary of data element tag information
            * group: Tag group of data element
            * element: Tag element of data element
            * str: String representation of data element tag """
    def __init__(self, swig_element, name, value):
        """ Executed on creation of Data Element

        :param swig_element: GDCMs DataElement object
        :param name: Name of DICOM Data Element
        :param value: Value of DICOM Data Element """
        self._swig_element = swig_element

        self.name = name
        self.value = value
        self.VR = str(swig_element.GetVR()).strip()
        self.VL = str(swig_element.GetVL()).strip()

        tg = swig_element.GetTag()
        self.tag = {
            "group": hex(int(tg.GetGroup())),
            "element": hex(int(tg.GetElement())),
            "str": str(swig_element.GetTag()).strip(),
        }

    def __repr__(self):
        return "<DataElement {0} {1}>".format(self.name, self.tag['str'])

    def __str__(self):
        return str(self.name)


class Dicom(object):
    """ Primary class that loads the DICOM file into memory and has properties
    that allows for reading the DICOM elements, extracting images

    :param fname: Location and filename of DICOM file.
    """
    def __init__(self, fname):
        self.fname = fname
        self.file_name, self.file_extension = os.path.splitext(fname)

        reader = gdcm.Reader()
        reader.SetFileName(fname)
        if not reader.Read():
            raise InvalidDicom("Not a valid DICOM file")

        self._file = reader.GetFile()
        self._header = self._file.GetHeader()
        self._dataset = self._file.GetDataSet()
        self._str_filter = gdcm.StringFilter()
        self._str_filter.SetFile(self._file)

        self._image = None
        self._anon_obj = None
        self._errors = None
        self._warnings = None

    def __repr__(self):
        return "<Dicom {0}>".format(self.fname)

    def __str__(self):
        return str(self.fname)

    def read(self):
        """ Returns array of dictionaries containing all the data elements in
        the DICOM file.
        """
        def ds(data_element):
            value = self._str_filter.ToStringPair(data_element.GetTag())
            if value[1]:
                return DataElement(data_element, value[0].strip(), value[1].strip())

        results = [data for data in self.walk(ds) if data is not None]
        return results

    def walk(self, fn):
        """ Loops through all data elements and allows a function to interact
        with each data element.  Uses a generator to improve iteration.

        :param fn: Function that interacts with each DICOM element """
        if not hasattr(fn, "__call__"):
            raise TypeError("""walk_dataset requires a
                function as its parameter""")

        dataset = self._dataset
        iterator = dataset.GetDES().begin()
        while (not iterator.equal(dataset.GetDES().end())):
            data_element = iterator.next()
            yield fn(data_element)

        header = self._header
        iterator = header.GetDES().begin()
        while (not iterator.equal(header.GetDES().end())):
            data_element = iterator.next()
            yield fn(data_element)

    def find(self, group=None, element=None, name=None, VR=None):
        """ Searches for data elements in the DICOM file given the filters
        supplied to this method.

        :param group: Hex decimal for the group of a DICOM element e.g. 0x002
        :param element: Hex decimal for the element value of a DICOM element e.g. 0x0010
        :param name: Name of the DICOM element, e.g. "Modality"
        :param VR: Value Representation of the DICOM element, e.g. "PN"
        """
        results = self.read()

        if name is not None:
            def find_name(data_element):
                return data_element.name.lower() == name.lower()
            return filter(find_name, results)

        if group is not None:
            def find_group(data_element):
                return (data_element.tag['group'] == group
                        or int(data_element.tag['group'], 16) == group)
            results = filter(find_group, results)

        if element is not None:
            def find_element(data_element):
                return (data_element.tag['element'] == element
                        or int(data_element.tag['element'], 16) == element)
            results = filter(find_element, results)

        if VR is not None:
            def find_VR(data_element):
                return data_element.VR.lower() == VR.lower()
            results = filter(find_VR, results)

        return results

    def anonymize(self):
        """ According to PS 3.15-2008, basic application level
        De-Indentification of a DICOM file requires replacing the values of a
        set of data elements"""
        self._anon_obj = gdcm.Anonymizer()
        self._anon_obj.SetFile(self._file)
        self._anon_obj.RemoveGroupLength()

        if self._anon_tags is None:
            self._anon_tags = get_anon_tags()

        for tag in self._anon_tags:
            cur_tag = tag['Tag'].replace("(", "")
            cur_tag = cur_tag.replace(")", "")
            name = tag["Attribute Name"].replace(" ", "").encode("utf8")
            group, element = cur_tag.split(",", 1)

            # TODO expand this 50xx, 60xx, gggg, eeee
            if ("xx" not in group
                and "gggg" not in group
                and "eeee" not in group):
                    group = int(group, 16)
                    element = int(element, 16)
                    if self.find(group=group, element=element):
                        self._anon_obj.Replace(
                            gdcm.Tag(group, element), "Anon" + name)

        return self._anon_obj

    def save_as(self, fname, obj=None):
        """ Save DICOM file given a GDCM DICOM object.
        Examples of a GDCM DICOM object:
        * gdcm.Writer()
        * gdcm.Reader()
        * gdcm.Anonymizer()

        :param fname: DICOM file name to be saved
        :param obj: DICOM object to be saved, if None, Anonymizer() is used
        """
        writer = gdcm.Writer()
        writer.SetFileName(fname)
        if obj is None and self._anon_obj:
            obj = self._anon_obj
        else:
            raise ValueError("Need DICOM object, e.g. obj=gdcm.Anonymizer()")
        writer.SetFile(obj.GetFile())
        if not writer.Write():
            raise IOError("Could not save DICOM file")
        return True

    @property
    def image(self):
        """ Read the loaded DICOM image data """
        if self._image is None:
            self._image = Image(self.fname)
        return self._image

    def validate(self):
        validation = validate(self.fname)
        self._errors = validation['errors']
        self._warnings = validation['warnings']
        return validation

    @property
    def errors(self):
        if self._errors is None:
            return self.validate()['errors']
        return self._errors

    @property
    def warnings(self):
        if self._warnings is None:
            return self.validate()['warnings']
        return self._warnings
