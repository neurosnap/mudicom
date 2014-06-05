import unittest
import gdcm
from mudicom import Read, Image


class TestImage(unittest.TestCase):

	def setUp(self):
		self.fnames = ("dicoms/ex1.dcm", "dicoms/ex2.dcm",)


if __name__ == '__main__':
	unittest.main(verbosity=2)
