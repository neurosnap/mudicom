import os.path
import unittest
import gdcm

import mudicom


class TestValidate(unittest.TestCase):

	def setUp(self):
		nose_dir = os.path.join(os.path.dirname(os.path.realpath(__file__)), "dicoms")
		self.fnames = (os.path.join(nose_dir, "ex1.dcm"),
						os.path.join(nose_dir, "ex2.dcm"),)

	def test_base_validate(self):
		dcm = mudicom.validate(self.fnames[0])
		self.assertEqual(len(dcm['errors']), 6)
		self.assertEqual(len(dcm['warnings']), 18)

		dcm = mudicom.validate(self.fnames[1])
		self.assertEqual(len(dcm['errors']), 7)
		self.assertEqual(len(dcm['warnings']), 18)

	def test_dicom_class_validate(self):
		mu = mudicom.load(self.fnames[0])
		dcm = mu.validate()
		self.assertEqual(len(dcm['errors']), 6)
		self.assertEqual(len(dcm['warnings']), 18)

		mu = mudicom.load(self.fnames[1])
		dcm = mu.validate()
		self.assertEqual(len(dcm['errors']), 7)
		self.assertEqual(len(dcm['warnings']), 18)