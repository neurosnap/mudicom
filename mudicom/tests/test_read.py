import os.path
import unittest
import gdcm

import mudicom


class TestRead(unittest.TestCase):

	def setUp(self):
		nose_dir = os.path.join("mudicom", "tests", "dicoms")
		self.fnames = (os.path.join(nose_dir, "ex1.dcm"),
			os.path.join(nose_dir, "ex2.dcm"),)

	def test_get_dataset(self):
		for fname in self.fnames:
			mu = mudicom.load(fname)
			ds = mu.read()
			self.assertIsInstance(ds, list)
			self.assertIsNot(len(ds), 0)

			for element in ds:
				self.assertTrue(hasattr(element, "name"))
				self.assertTrue(hasattr(element, "value"))
				self.assertTrue(hasattr(element, "VR"))
				self.assertTrue(hasattr(element, "VL"))
				self.assertTrue(hasattr(element, "tag"))
				self.assertTrue("group" in element.tag)
				self.assertTrue("element" in element.tag)
				self.assertTrue("str" in element.tag)

	def test_map_VR(self):
		self.assertEqual(mudicom.lookup_VR(VR="AE"), "Application Entity")
		self.assertEqual(mudicom.lookup_VR("OB"), "Other Byte")
		self.assertEqual(mudicom.lookup_VR("US"), "Unsigned Short")
		self.assertEqual(mudicom.lookup_VR(description="Time"), "TM")
		self.assertEqual(mudicom.lookup_VR(description="Unknown"), "UN")
		self.assertEqual(mudicom.lookup_VR(description="Sequence of Items"), "SQ")
		self.assertRaises(Exception, mudicom.lookup_VR, "ZZ")
		self.assertRaises(Exception, mudicom.lookup_VR, None, "Hi there")


	def test_walk_dataset(self):
		for fname in self.fnames:
			mu = mudicom.load(fname)
			#reader = mu.read()

			tags = list(mu.walk(lambda ds: ds.GetTag()))
			self.assertIsInstance(tags, list)
			self.assertIsNot(len(tags), 0)
			for tag in tags:
				self.assertIsInstance(tag, gdcm.Tag)

			tags = list(mu.walk(lambda ds: None))
			self.assertIsInstance(tags, list)
			for tag in tags:
				self.assertEqual(tag, None)

			tags = list(mu.walk(lambda ds: False))
			self.assertIsInstance(tags, list)
			for tag in tags:
				self.assertFalse(tag)

			tags = list(mu.walk(lambda ds: True))
			self.assertIsInstance(tags, list)
			for tag in tags:
				self.assertTrue(tag)

	def test_get_element(self):
		for fname in self.fnames:
			mu = mudicom.load(fname)
			#reader = mu.read()
			self.assertIsInstance(mu.find(0x004, 0x1220), list)
			self.assertIsInstance(mu.find(name="Modality"), list)
			self.assertIsInstance(mu.find(VR="PN"), list)
