import os
import sys
import unittest
import gdcm
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(os.path.realpath(__file__)), os.pardir)))
from dicomimg import Reader

# DICOM files to test
fnames = ("dicoms/ex1.dcm", "dicoms/ex2.dcm",)
types = ("hi there", 0, 123213, {}, [], (), True, False)

class TestReader(unittest.TestCase):

	def setUp(self):
		pass

	def test_get_dataset(self):
		for fname in fnames:
			reader = Reader(fname)
			ds = reader.get_dataset()
			self.assertIsInstance(ds, tuple)
			self.assertIsNot(len(ds), 0)

			for element in ds:
				self.assertTrue("name" in element)
				self.assertTrue("tag" in element)
				self.assertTrue("value" in element)
				self.assertTrue("value_repr" in element)
				self.assertTrue("value_length" in element)

	def test_map_VR(self):
		for fname in fnames:
			reader = Reader(fname)
			self.assertEqual(reader.map_VR("AE"), "Application Entity")
			self.assertEqual(reader.map_VR("OB"), "Other Byte")
			self.assertEqual(reader.map_VR("US"), "Unsigned Short")

	def test_walk_dataset(self):
		for fname in fnames:
			reader = Reader(fname)

			tags = reader.walk_dataset(lambda ds: ds.GetTag())
			self.assertIsInstance(tags, list)
			self.assertIsNot(len(tags), 0)
			for tag in tags:
				self.assertIsInstance(tag, gdcm.Tag)

			tags = reader.walk_dataset(lambda ds: None)
			self.assertIsInstance(tags, list)
			for tag in tags:
				self.assertEqual(tag, None)

			tags = reader.walk_dataset(lambda ds: False)
			self.assertIsInstance(tags, list)
			for tag in tags:
				self.assertFalse(tag)

			tags = reader.walk_dataset(lambda ds: True)
			self.assertIsInstance(tags, list)
			for tag in tags:
				self.assertTrue(tag)

			for flavor in types:
				self.assertRaises(Exception, reader.walk_dataset, flavor)

	def test_get_element(self):
		for fname in fnames:
			reader = Reader(fname)
			self.assertIsInstance(reader.get_element((0x004, 0x1220)), dict)
			self.assertIsInstance(reader.get_element(name="Modality"), dict)
			self.assertIsInstance(reader.get_element(VR="PN"), tuple)

		
if __name__ == '__main__':
	unittest.main(verbosity=2)