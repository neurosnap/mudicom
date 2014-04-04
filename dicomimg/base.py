"""
Abstract class that Image, Validator, and Reader inherit
"""

class BaseDicom():
	
	def __init__(self, fname):
		self.fname = fname

	def __repr__(self):
		return repr(self.fname)