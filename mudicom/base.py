import os
import gdcm

from .image import Image


class DataElement(object):
    """ Object representation of a Data Element

    :param swig_element: GDCMs DataElement SWIG object
    :param name: Name of DICOM data element
    :param value: Value of DICOM data element

    DataElement Properties:
        name: Name of DICOM data element
        Value: Value of data element
        VR: Value Representation of data element
        VL: Value Length of data element
        tag: Dictionary of data element tag information
        tag['group']: Tag group of data element
        tag['element']: Tag element of data element
        tag['str']: String representation of data element tag """

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
        return self.name


class Dicom(object):
    """ Primary class that loads the DICOM file into
    memory and has properties that allows for reading
    the DICOM elements, extracting images

    :param fname: Location and filename of DICOM file.
    """
    def __init__(self, fname):
        self.fname = fname
        self.file_name, self.file_extension = os.path.splitext(fname)

        reader = gdcm.Reader()
        reader.SetFileName(fname)
        if not reader.Read():
            raise Exception("Not a valid DICOM file")

        file_mem = reader.GetFile()
        self._header = file_mem.GetHeader()
        self._dataset = file_mem.GetDataSet()
        self._str_filter = gdcm.StringFilter()
        self._str_filter.SetFile(file_mem)

    def __repr__(self):
        return "<Dicom {0}>".format(self.fname)

    def __str__(self):
        return str(self.fname)

    def image(self):
        """ Read the loaded DICOM image data """
        return Image(self.fname)

    def read(self):
        """ Returns array of dictionaries containing
        all the data elements in the DICOM file.
        """
        def ds(data_element):
            value = self._str_filter.ToStringPair(data_element.GetTag())
            if value[1]:
                return DataElement(data_element, value[0].strip(), value[1].strip())

        results = [data for data in self.walk(ds) if data is not None]
        return results

    def walk(self, fn):
        """ Loops through all data elements and
        allows a function to interact with each data element.  Uses
        a generator to improve iteration.

        :param fn: Function that interacts with each DICOM element """
        if not hasattr(fn, "__call__"):
            raise Exception("""walk_dataset requires a
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
        """ Searches for data elements in the DICOM file given
        the filters supplied to this method.

        :param group: Hex decimal for the group of a DICOM element e.g. 0x002
        :param element: Hex decimal for the element value of a
        DICOM element e.g. 0x0010
        :param name: Name of the DICOM element, e.g. "Modality"
        :param VR: Value Representation of the DICOM element, e.g. "PN"
        """
        results = self.read()

        if name is not None:
            def find_name(data_element):
                if data_element.name.lower() == name.lower():
                    return True
                else:
                    return False
            return filter(find_name, results)

        if group is not None:
            def find_group(data_element):
                if (data_element.tag['group'] == group
                    or int(data_element.tag['group'], 16) == group):
                        return True
                else:
                    return False
            results = filter(find_group, results)

        if element is not None:
            def find_element(data_element):
                if (data_element.tag['element'] == element
                    or int(data_element.tag['element'], 16) == element):
                        return True
                else:
                    return False
            results = filter(find_element, results)

        if VR is not None:
            def find_VR(data_element):
                if data_element.VR.lower() == VR.lower():
                    return True
                else:
                    return False
            results = filter(find_VR, results)

        return results