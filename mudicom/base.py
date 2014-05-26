"""
Abstract class that Image, Validator, and Reader inherit
"""
import os
import gdcm

class BaseDicom(object):
	
	def __init__(self, fname):
		self.fname = fname
		self.file_name, self.file_extension = os.path.splitext(fname)
		self.gdcm = gdcm
		
		reader = gdcm.Reader()
		reader.SetFileName(fname)
		if not reader.Read():
			raise Exception("Not a valid DICOM file")

		self.file = reader.GetFile()

		self.str_filter = gdcm.StringFilter()
		self.str_filter.SetFile(reader.GetFile())

	def __repr__(self):
		return repr(self.fname)