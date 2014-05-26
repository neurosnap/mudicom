import gdcm
from .base import BaseDicom


class Reader(BaseDicom):

	def __init__(self, fname):
		super(Reader, self).__init__(fname)
		self.get_dataset()

	def get_element(self, group=None, element=None, name=None, VR=None):
		""" Finds a data element in the DICOM file """
		results = self.dataset
		if group is not None:
			def find_group(data_element):
				if (data_element['tag_group'] == group 
					or int(data_element['tag_group'], 16) == group):
						return True
				else:
					return False
			results = filter(find_group, results)

		if element is not None:
			def find_element(data_element):
				if (data_element['tag_element'] == element
					or int(data_element['tag_element'], 16) == element):
						return True
				else:
					return False
			results = filter(find_element, results)

		return results

	def get_dataset(self):
		""" Returns array of dictionaries containing
		all the data elements in the DICOM
		"""
		if hasattr(self, "dataset"):
			return self.dataset

		def ds(data_element):
			tg = data_element.GetTag()
			value = self.str_filter.ToStringPair(data_element.GetTag())
			if value[1]:
				value_repr = str(data_element.GetVR()).strip()
				dict_element = {
					"name": value[0].strip(),
					"tag_group": hex(int(tg.GetGroup())),
					"tag_element": hex(int(tg.GetElement())),
					"tag_str": str(data_element.GetTag()).strip(),
					"value": value[1].strip(),
					"value_repr": value_repr,
					"value_length": str(data_element.GetVL()).strip()
				}

				return dict_element

		self.dataset = [data for data in self.walk_dataset(ds) if data is not None]
		return self.dataset

	def walk_dataset(self, fn):
		""" Loops through all data elements and
		allows a function to interact with each data element """
		if not hasattr(fn, "__call__"):
			raise Exception("walk_dataset requires a function as its parameter")

		dataset = self.file.GetDataSet()
		iterator = dataset.GetDES().begin()
		while (not iterator.equal(dataset.GetDES().end())):
			data_element = iterator.next()
			yield fn(data_element)

	def map_VR(self, VR=None, description=None):
		""" Value Representation (VR) lookup """
		value_repr = {
			"AE": "Application Entity",
			"AS": "Age String",
			"AT": "Attribute Tag",
			"CS": "Code String",
			"DA": "Date",
			"DS": "Decimal String",
			"DT": "Date/Time",
			"FL": "Floating Point Single (4 bytes)",
			"FD": "Floating Point Double (8 bytes)",
			"IS": "Integer String",
			"LO": "Long String",
			"LT": "Long Text",
			"OB": "Other Byte",
			"OF": "Other Float",
			"OW": "Other Word",
			"PN": "Person Name",
			"SH": "Short String",
			"SL": "Signed Long",
			"SQ": "Sequence of Items",
			"SS": "Signed Short",
			"ST": "Short Text",
			"TM": "Time",
			"UI": "Unique Identifier",
			"UL": "Unsigned Long",
			"UN": "Unknown",
			"US": "Unsigned Short",
			"UT": "Unlimited Text"
		}
		if VR:
			if VR in value_repr:
				return value_repr[VR]
			else:
				raise Exception("VR not found in map")
		elif description:
			for key, value in value_repr.iteritems():
				if description == value:
					return key
			raise Exception("Description not found in map")
		else:
			raise Exception("Either VR or description required to map_VR")
