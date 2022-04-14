from .main import main

def static(*args, Fs_N, **kwargs):
	"""Calculates static factor of safety. Calls main to recalculate spring parameters, then peforms factor of safety calculation"""

	mainCalc = main(**kwargs)

	responseData = {
			"n_s_": Fs_N
	}

	return responseData