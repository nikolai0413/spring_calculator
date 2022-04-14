from .main import main

def fatigue(*args, F_max_N, F_min_N, **kwargs):
		"""Calculates static factor of safety. Calls main to recalculate spring parameters, then peforms factor of safety calculation"""
		
		mainResult = main(**kwargs)




		responseData = {
			"n_f_": F_max_N + F_min_N
		}

		return responseData