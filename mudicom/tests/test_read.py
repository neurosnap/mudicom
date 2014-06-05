import unittest
import gdcm
from mudicom import Read

# DICOM files to test
fnames = ("dicoms/ex1.dcm", "dicoms/ex2.dcm",)
types = ("hi there", 0, 123213, {}, [], (), True, False)

class TestRead(unittest.TestCase):

	def setUp(self):
		pass

	def test_get_dataset(self):
		for fname in fnames:
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
		reader = Read(fnames[0])
		self.assertEqual(reader.map_VR(VR="AE"), "Application Entity")
		self.assertEqual(reader.map_VR("OB"), "Other Byte")
		self.assertEqual(reader.map_VR("US"), "Unsigned Short")
		self.assertEqual(reader.map_VR(description="Time"), "TM")
		self.assertEqual(reader.map_VR(description="Unknown"), "UN")
		self.assertEqual(reader.map_VR(description="Sequence of Items"), "SQ")
		self.assertRaises(Exception, reader.map_VR, "ZZ")
		self.assertRaises(Exception, reader.map_VR, None, "Hi there")


	def test_walk_dataset(self):
		for fname in fnames:
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

			#for flavor in types:
			#	self.assertRaises(Exception, list(reader.walk_dataset), flavor)

	def test_get_element(self):
		for fname in fnames:
			reader = Read(fname)
			self.assertIsInstance(reader.get_element(0x004, 0x1220), list)
			self.assertIsInstance(reader.get_element(name="Modality"), list)
			self.assertIsInstance(reader.get_element(VR="PN"), list)

if __name__ == '__main__':
	unittest.main(verbosity=2)
