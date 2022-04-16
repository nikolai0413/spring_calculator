from .main import MainCalculate
import numpy as np


def static(*args, Fstatic_lbf, **kwargs):
    """Calculates static factor of safety. Calls main to recalculate spring parameters, then peforms factor of safety calculation"""

    sc = StaticCalculate(Fstatic_lbf, **kwargs)

    return sc.doStaticCalc(True)


class StaticCalculate(MainCalculate):
    def __init__(
        self, Fstatic_lbf, material, endType, wireDiameter_in, OD_in, L0_in, Ls_in
    ):
        super().__init__(material, endType, wireDiameter_in, OD_in, L0_in, Ls_in)

        # INPUTS
        self.Fstatic_lbf = Fstatic_lbf

        # OUTPUTS
        self.nStatic_ = None

    def doStaticCalc(self, returnResults=False):
        """Does static calculation"""
        # first calculate main
        self.calculateMain()

        tauFInput_psi = (
            self.kB_
            * 8
            * self.Fstatic_lbf
            * self.meanDiam_in
            / (np.pi * self.wireDiameter_in**3)
        )
        self.nStatic_ = self.sSY_psi / tauFInput_psi

        if returnResults:
            return {"nStatic_": self.nStatic_}
