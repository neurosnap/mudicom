import gdcm
from .base import BaseDicom


class Anonymity(BaseDicom):
    """ This class uses dciodvfy to generate 
    a list of warnings and errors discovered within
    the DICOM file.

    :param fname: Location and filename of DICOM file.
    """
    def __init__(self, fname):
        super(Anonymity, self).__init__(fname)