

class CalculationError(Exception):
		"""When the calculation fails such as due to inputs being out of range"""
		def __init__(self, message=None):
			self.message = message