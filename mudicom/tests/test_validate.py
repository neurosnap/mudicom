import os.path
import unittest
import gdcm

from .. import Validate

class TestValidate(unittest.TestCase):

	def setUp(self):
		nose_dir = os.path.join("mudicom", "tests", "dicoms")
		self.fnames = (os.path.join(nose_dir, "ex1.dcm"), 
			os.path.join(nose_dir, "ex2.dcm"),)

	def test_init(self):
		dcm = Validate(self.fnames[0])
		self.assertEqual(len(dcm.get_errors()), 6)
		self.assertEqual(len(dcm.get_warnings()), 18)

		dcm = Validate(self.fnames[1])
		self.assertEqual(len(dcm.get_errors()), 7)
		self.assertEqual(len(dcm.get_warnings()), 18)