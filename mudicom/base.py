import os
import pprint
import gdcm

from .image import Image


class Dicom(object):
    """ Primary class that loads the DICOM file into 
    memory and has properties that allows for reading
    the DICOM elements, saving an image, and
    validation

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

        self._pretty = pprint.PrettyPrinter(indent=4)

    def image(self):
        """ Read the loaded DICOM image data """
        return Image(self.fname)

    def read(self, pretty=False):
        """ Returns array of dictionaries containing
        all the data elements in the DICOM file.
        """
        def ds(data_element):
            tg = data_element.GetTag()
            value = self._str_filter.ToStringPair(data_element.GetTag())
            if value[1]:
                value_repr = str(data_element.GetVR()).strip()
                dict_element = {
                    "name": value[0].strip(),
                    "tag": {
                        "group": hex(int(tg.GetGroup())),
                        "element": hex(int(tg.GetElement())),
                        "str": str(data_element.GetTag()).strip(),
                    },
                    "value": value[1].strip(),
                    "VR": value_repr,
                    "VL": str(data_element.GetVL()).strip()
                }

                return dict_element
        results = [data for data in self.walk(ds) if data is not None]
        if pretty:
            return self._pretty.pprint(results)
        else:
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

    def find(self, group=None, element=None, name=None, VR=None, pretty=False):
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
                if data_element['name'].lower() == name.lower():
                    return True
                else:
                    return False
            return filter(find_name, results)

        if group is not None:
            def find_group(data_element):
                if (data_element['tag']['group'] == group
                    or int(data_element['tag']['group'], 16) == group):
                        return True
                else:
                    return False
            results = filter(find_group, results)

        if element is not None:
            def find_element(data_element):
                if (data_element['tag']['element'] == element
                    or int(data_element['tag']['element'], 16) == element):
                        return True
                else:
                    return False
            results = filter(find_element, results)

        if VR is not None:
            def find_VR(data_element):
                if data_element['VR'].lower() == VR.lower():
                    return True
                else:
                    return False
            results = filter(find_VR, results)

        if pretty:
            return self._pretty.pprint(results)
        else:
            return results

    def write(self, data_element, value=None, VR=None, VL=None):
        """ Write a value into the data element

        data_element.SetValue()
        data_element.SetVR()
        data_element.SetVL()
        """
        if value is not None:
            pass

        if VR is not None:
            pass

        if VL is not None:
            pass

    def anonymize(self):
        """ Scrubs all patient information
        from the DICOM object in memory
        """

    def save(self, fname):
        """ Saves DICOM file from memory

        :param fname: Location and file of DICOM file to be saved.
        """