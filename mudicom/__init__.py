import os

__version__ = '0.0.1'
__liscense__ = 'MIT'
__author__ = 'Eric Bower'

PACKAGE_DIR = os.path.dirname(os.path.abspath(__file__))

from .base import BaseDicom
from .image import Image
from .validator import Validator
from .reader import Reader