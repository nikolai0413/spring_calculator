import numpy as np

def main(*args, material, endType, wireDiameter_in, OD_in, L0_in, Ls_in):
    """Performs primary or 'main' calculation for the app. Returns python dict"""

    
		# TODO calculation



    # TODO update return value
    responseData = {
        "pitch_in_rev": wireDiameter_in,
        "nt_": OD_in,
        "na_": L0_in,
        "k_lbf_in": Ls_in,
        "Fls_lbf": wireDiameter_in,
        "n_ls_": wireDiameter_in,
    }
		
    return responseData
