import numpy as np
from .main import MainCalculate, main

def fatigue(*args, F_max_lbf, F_min_lbf, **kwargs):
	"""Calculates fatigue factor of safety. Calls main to recalculate spring parameters, then peforms factor of safety calculation"""

	fc = FatigueCalculate(F_max_lbf, F_min_lbf, **kwargs)

	return fc.doFatigueCalc(True)

class FatigueCalculate(MainCalculate):
	def __init__(self, F_max_lbf, F_min_lbf, material, endType, wireDiameter_in, OD_in, L0_in, Ls_in):
		super().__init__( material, endType, wireDiameter_in, OD_in, L0_in, Ls_in)

		# INPUTS
		self.F_max_lbf = F_max_lbf
		self.F_min_lbf = F_min_lbf

		# OUTPUTS
		self.nFatigue_

	
	def doFatigueCalc(self, returnResult=False):
		"""Performs fatigue calculates. Calls main first"""
		# call main calculation first
		self.calculateMain()
		
		fA_lbf = (self.F_max_lbf - self.F_min_lbf)/2
		fM_lbf = (self.F_max_lbf + self.F_min_lbf)/2

		tA_psi = self.kB_ * 8 * fA_lbf * self.meanDiam_in / (np.pi * self.wireDiameter_in**3)
		tM_psi = self.kB_ * 8 * fM_lbf * self.meanDiam_in / (np.pi * self.wireDiameter_in**3)

		sSA_psi = 35000 # Unpeened
		sSM_psi = 55000 # Unpeened
		sSU_psi = 0.67 * self.uts_psi# Unpeened

		sSE_psi = sSA_psi / (1 - sSM_psi / sSU_psi)

		self.nFatigue_ = (tA_psi/sSE_psi + tM_psi/sSU_psi)**(-1)

		if returnResult:
			return {
				"nFatigue_": self.nFatigue_
			}