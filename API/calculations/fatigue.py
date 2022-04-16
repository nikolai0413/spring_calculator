from .main import main

def fatigue(*args, F_max_lbf, F_min_lbf, **kwargs):
	"""Calculates fatigue factor of safety. Calls main to recalculate spring parameters, then peforms factor of safety calculation"""

	# get main results since static calculation needs that info
	mainResults = main(**kwargs)

	# TODO calculation	


	# TODO update return value
	responseData = {
		"nFatigue_": F_max_lbf + F_min_lbf
	}

	return responseData