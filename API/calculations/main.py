def main(*args, material, endType, wireDiameter_mm, OD_mm, L0_mm, Ls_mm):
    """Performs primary or 'main' calculation for the app. Returns python dict"""

		# TODO calculation


    responseData = {
        "pitch_mm": wireDiameter_mm,
        "nt_": OD_mm,
        "na_": L0_mm,
        "k_N_m": Ls_mm,
        "F_ls_N": wireDiameter_mm,
        "n_ls_": wireDiameter_mm,
    }
		
    return responseData
