import os
import gdcm

from .image import Image


class BaseDicom(object):
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

        self.file = reader.GetFile()
        self.str_filter = gdcm.StringFilter()
        self.str_filter.SetFile(self.file)

    def image(self):
        """ Read the loaded DICOM image data """
        return Image(self.fname)

    def read(self):
        """ Returns array of dictionaries containing
        all the data elements in the DICOM file.
        """
        def ds(data_element):
            tg = data_element.GetTag()
            value = self.str_filter.ToStringPair(data_element.GetTag())
            if value[1]:
                value_repr = str(data_element.GetVR()).strip()
                dict_element = {
                    "name": value[0].strip(),
                    "tag_group": hex(int(tg.GetGroup())),
                    "tag_element": hex(int(tg.GetElement())),
                    "tag_str": str(data_element.GetTag()).strip(),
                    "value": value[1].strip(),
                    "value_repr": value_repr,
                    "value_length": str(data_element.GetVL()).strip()
                }

                return dict_element

        return [data for data in self.walk(ds) if data is not None]

    def walk(self, fn):
        """ Loops through all data elements and
        allows a function to interact with each data element.  Uses
        a generator to improve iteration.

        :param fn: Function that interacts with each DICOM element """
        if not hasattr(fn, "__call__"):
            raise Exception("""walk_dataset requires a 
                function as its parameter""")

        dataset = self.file.GetDataSet()
        iterator = dataset.GetDES().begin()
        while (not iterator.equal(dataset.GetDES().end())):
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
        if group is not None:
            def find_group(data_element):
                if (data_element['tag_group'] == group
                    or int(data_element['tag_group'], 16) == group):
                        return True
                else:
                    return False
            results = filter(find_group, results)

        if element is not None:
            def find_element(data_element):
                if (data_element['tag_element'] == element
                    or int(data_element['tag_element'], 16) == element):
                        return True
                else:
                    return False
            results = filter(find_element, results)

        return results

    def anonymize(self):
        """ Scrubs all patient information
        from the DICOM object in memory
        """

    def save(self, fname):
        """ Saves DICOM file from memory

        :param fname: Location and file of DICOM file to be saved.
        """