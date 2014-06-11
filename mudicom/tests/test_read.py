import os.path
import unittest
import gdcm

from .. import Read


class TestRead(unittest.TestCase):

	def setUp(self):
		nose_dir = os.path.join("mudicom", "tests", "dicoms")
		self.fnames = (os.path.join(nose_dir, "ex1.dcm"), 
			os.path.join(nose_dir, "ex2.dcm"),)

	def test_get_dataset(self):
		for fname in self.fnames:
			reader = Read(fname)
			ds = reader.get_dataset()
			self.assertIsInstance(ds, list)
			self.assertIsNot(len(ds), 0)

			for element in ds:
				self.assertTrue("name" in element)
				self.assertTrue("tag_group" in element)
				self.assertTrue("tag_element" in element)
				self.assertTrue("tag_str" in element)
				self.assertTrue("value" in element)
				self.assertTrue("value_repr" in element)
				self.assertTrue("value_length" in element)

	def test_map_VR(self):
		reader = Read(self.fnames[0])
		self.assertEqual(reader.map_VR(VR="AE"), "Application Entity")
		self.assertEqual(reader.map_VR("OB"), "Other Byte")
		self.assertEqual(reader.map_VR("US"), "Unsigned Short")
		self.assertEqual(reader.map_VR(description="Time"), "TM")
		self.assertEqual(reader.map_VR(description="Unknown"), "UN")
		self.assertEqual(reader.map_VR(description="Sequence of Items"), "SQ")
		self.assertRaises(Exception, reader.map_VR, "ZZ")
		self.assertRaises(Exception, reader.map_VR, None, "Hi there")


	def test_walk_dataset(self):
		for fname in self.fnames:
			reader = Read(fname)

			tags = list(reader.walk_dataset(lambda ds: ds.GetTag()))
			self.assertIsInstance(tags, list)
			self.assertIsNot(len(tags), 0)
			for tag in tags:
				self.assertIsInstance(tag, gdcm.Tag)

			tags = list(reader.walk_dataset(lambda ds: None))
			self.assertIsInstance(tags, list)
			for tag in tags:
				self.assertEqual(tag, None)

			tags = list(reader.walk_dataset(lambda ds: False))
			self.assertIsInstance(tags, list)
			for tag in tags:
				self.assertFalse(tag)

			tags = list(reader.walk_dataset(lambda ds: True))
			self.assertIsInstance(tags, list)
			for tag in tags:
				self.assertTrue(tag)

	def test_get_element(self):
		for fname in self.fnames:
			reader = Read(fname)
			self.assertIsInstance(reader.get_element(0x004, 0x1220), list)
			self.assertIsInstance(reader.get_element(name="Modality"), list)
			self.assertIsInstance(reader.get_element(VR="PN"), list)
