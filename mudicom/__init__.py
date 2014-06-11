import os

PACKAGE_DIR = os.path.dirname(os.path.abspath(__file__))

from .image import Image
from .validate import Validate
from .read import Read
from .anonymity import Anonymity

def load(fname):
	""" Imports DICOM file into memory

	:param fname: Location and filename of DICOM file.
	"""