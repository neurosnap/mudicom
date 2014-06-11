import os
import unittest
import numpy
import gdcm

from .. import Read, Image


class TestImage(unittest.TestCase):

	def setUp(self):
		nose_dir = os.path.join("mudicom", "tests", "dicoms")
		self.fnames = (os.path.join(nose_dir, "ex1.dcm"), 
			os.path.join(nose_dir, "ex2.dcm"),)

	def test_get_numpy(self):
		for fname in self.fnames:
			dcm = Image(fname)
			gnp = dcm.get_numpy()
			self.assertIsInstance(gnp, numpy.ndarray)
			self.assertEqual(gnp.dtype, numpy.float)
