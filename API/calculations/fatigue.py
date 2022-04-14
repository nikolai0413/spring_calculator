from .main import main

def fatigue(*args, F_max_N, F_min_N, **kwargs):
	"""Calculates fatigue factor of safety. Calls main to recalculate spring parameters, then peforms factor of safety calculation"""

	# get main results since static calculation needs that info
	mainResults = main(**kwargs)

	# TODO calculation	


	# TODO update return value
	responseData = {
		"n_f_": F_max_N + F_min_N
	}

	return responseData