def main(params):
	print("Calclating Main")




	responseData = {
	"p": params['wireDiameter_mm'] + 1,
	"nt": params['wireDiameter_mm'] + 2,
	"na": params['wireDiameter_mm'] + 3,
	"k": params['wireDiameter_mm'] + 4,
	"F_ls": params['wireDiameter_mm'] + 5,
	"n_ls": params['wireDiameter_mm'] + 6,
	}


	return responseData