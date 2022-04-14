def static(params):
	print("Calculating Satic")
	print(params)
	responseData = {
			"n_s": params["Fs_N"] + 1
	}
	print(responseData)
	return responseData