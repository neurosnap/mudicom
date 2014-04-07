import re
import gdcm
from .base import BaseDicom

class Reader(BaseDicom):

	def get_element(self, tag=None, name=None, VR=None):
		""" Finds a data element in the DICOM file """

	def map_VR(self, VR=None, description=None):
		""" Value Representation (VR) lookup """

	def get_dataset(self):
		""" Returns array of dictionaries containing
		all the data elements in the DICOM
		"""
		if hasattr(self, "dataset"):
			return self.dataset

		def ds(data_element):
			value = self.str_filter.ToStringPair(data_element.GetTag())
			if value[1]:
				value_repr = str(data_element.GetVR()).strip()
				#tag = self.get_tag(data_element.GetTag())
				dict_element = {
					"name": value[0].strip(),
					"tag": str(data_element.GetTag()).strip(),
					"value": value[1].strip(),
					"value_repr": value_repr,
					"value_length": str(data_element.GetVL()).strip()
				}

				return dict_element

		self.dataset = tuple(self.walk_dataset(ds))
		return self.dataset

	def walk_dataset(self, fn):
		""" Loops through all data elements and
		allows a function to interact with each data element """
		if not hasattr(fn, "__call__"):
			raise Exception("walk_dataset requires a function as its parameter")

		dataset = self.file.GetDataSet()
		result = []
		iterator = dataset.GetDES().begin()
		while (not iterator.equal(dataset.GetDES().end())):
			data_element = iterator.next()
			res = fn(data_element)
			if res:
				result.append(res)

		return result
