from .main import main

def static(*args, Fs_N, **kwargs):
	"""Calculates static factor of safety. Calls main to recalculate spring parameters, then peforms factor of safety calculation"""

	# get main results since static calculation needs that info
	mainResults = main(**kwargs)


	# TODO static calculation


	# TODO update return value
	responseData = {
		"n_s_": Fs_N
	}

	return responseData