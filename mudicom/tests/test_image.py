import os
import unittest
import numpy
import gdcm

import mudicom


class TestImage(unittest.TestCase):

	def setUp(self):
		nose_dir = os.path.join(os.path.dirname(os.path.realpath(__file__)), "dicoms")
		self.fnames = (os.path.join(nose_dir, "ex1.dcm"),
			os.path.join(nose_dir, "ex2.dcm"),)

	def test_get_numpy(self):
		for fname in self.fnames:
			mu = mudicom.load(fname)
			img = mu.image()
			gnp = img.numpy()
			self.assertIsInstance(gnp, numpy.ndarray)
			self.assertEqual(gnp.dtype, numpy.float)
