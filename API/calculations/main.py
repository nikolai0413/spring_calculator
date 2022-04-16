from urllib import response
from .util import CalculationError
import numpy as np


def main(*args, material, endType, wireDiameter_in, OD_in, L0_in, Ls_in):
    """Performs primary or 'main' calculation for the app. Returns python dict"""

    mc = MainCalculate(material, endType, wireDiameter_in, OD_in, L0_in, Ls_in)
    
    return mc.calculateMain(True)


class MainCalculate:
    def __init__(self, material, endType, wireDiameter_in, OD_in, L0_in, Ls_in):
        # Inputs
        self.material = material
        self.endType = endType
        self.wireDiameter_in = wireDiameter_in
        self.OD_in = OD_in
        self.L0_in = L0_in
        self.Ls_in = Ls_in

        # Outputs
        self.pitch_in_rev = None
        self.nt_ = None
        self.na_ = None
        self.k_lbf_in = None
        self.fShut_lbf = None
        self.nShut_ = None
        self.nStatic_ = None
        self.nFatigue_ = None

        # Other Vars
        self.uts_psi = None
        self.G_Mlbf_in2 = None
        self.kB_ = None
        self.sSY_psi = None

    def calculateMain(self, returnResults=False):
        """Runs main calculation, optionally returns result"""
        self.computeEndType()
        self.computeUTS()
        self.getG()
        self.calcMeanDiam()
        self.calcSpringRate()
        self.calc_sSY()
        self.calcShutVals()

        if returnResults:
            return {
                "pitch_in_rev": self.pitch_in_rev,
                "nt_": self.nt_,
                "na_": self.na_,
                "k_lbf_in": self.k_lbf_in,
                "fShut_lbf": self.fShut_lbf,
                "nShut_": self.nShut_,
            }

    def computeEndType(self, testing=False):
        """Performs calculations related to end type selection"""
        if self.endType == "plain":
            nEnd_ = 0
            self.nt_ = self.Ls_in / self.wireDiameter_in - 1
            self.na_ = self.nt_ - nEnd_
            self.pitch_in_rev = (self.L0_in - self.wireDiameter_in) / self.na_

        elif self.endType == "plainAndGround":
            nEnd_ = 1
            self.nt_ = self.Ls_in / self.wireDiameter_in
            self.na_ = self.nt_ - nEnd_
            self.pitch_in_rev = (self.L0_in) / (self.na_ + 1)

        elif self.endType == "squaredOrClosed":
            nEnd_ = 2
            self.nt_ = self.Ls_in / self.wireDiameter_in - 1
            self.na_ = self.nt_ - nEnd_
            self.pitch_in_rev = (self.L0_in - 3 * self.wireDiameter_in) / self.na_

        elif self.endType == "squaredAndGround":
            nEnd_ = 2
            self.nt_ = self.Ls_in / self.wireDiameter_in
            self.na_ = self.nt_ - nEnd_
            self.pitch_in_rev = (self.L0_in - 2 * self.wireDiameter_in) / self.na_
        else:
            raise CalculationError("End type incorrect value")

        if testing:
            return nEnd_

    def computeUTS(self, testing=False):
        """Gets UTS based on material type"""

        # Shigley 10-4: "ASTM Code", exponent m, d_min [in], d_max [in], A kpsi-in
        propTable10_4 = np.array(
            [
                [0.145, 0.004, 0.256, 201.0],  # 0 "A228",
                [0.187, 0.02, 0.5, 147.0],  # 1 "A229",
                [0.19, 0.028, 0.5, 140.0],  # 2 "A227",
                [0.168, 0.032, 0.437, 169.0],  # 3 "A232",
                [0.108, 0.063, 0.375, 202.0],  # 4 "A401",
                [0.146, 0.013, 0.1, 169.0],  # 5 "A313",
                [0.263, 0.1, 0.2, 128.0],  # 6  "A313",
                [0.478, 0.2, 0.4, 90.0],  # 7  "A313",
                [0.0, 0.004, 0.022, 145.0],  # 8 "B159",
                [0.028, 0.022, 0.075, 121.0],  # 9 "B159",
                [0.064, 0.075, 0.3, 110.0],  # 10 "B159",
            ]
        )
        row = None

        if self.material == "A228":
            row = 0
        elif self.material == "A227":
            row = 2
        elif self.material == "A232":
            row = 3
        elif self.material == "A401":
            row = 4

        elif self.material == "A313":
            # further select based on wire diameter
            if self.wireDiameter_in < propTable10_4[5, 1]:
                raise CalculationError(
                    "Wire diameter "
                    + str(self.wireDiameter_in)
                    + " out of range for material "
                    + self.material
                )
            elif propTable10_4[5, 1] <= self.wireDiameter_in < propTable10_4[5, 2]:
                row = 5
            elif propTable10_4[6, 1] <= self.wireDiameter_in < propTable10_4[6, 2]:
                row = 6
            elif propTable10_4[7, 1] <= self.wireDiameter_in <= propTable10_4[7, 2]:
                row = 7
            else:
                raise CalculationError(
                    "Wire diameter "
                    + str(self.wireDiameter_in)
                    + " out of range for material "
                    + self.material
                )

        elif self.material == "B159":
            # further select based on wire diameter
            if self.wireDiameter_in < propTable10_4[8, 1]:
                raise CalculationError(
                    "Wire diameter "
                    + str(self.wireDiameter_in)
                    + " out of range for material "
                    + self.material
                )
            elif propTable10_4[8, 1] <= self.wireDiameter_in < propTable10_4[8, 2]:
                row = 8
            elif propTable10_4[9, 1] <= self.wireDiameter_in < propTable10_4[9, 2]:
                row = 9
            elif propTable10_4[10, 1] <= self.wireDiameter_in <= propTable10_4[10, 2]:
                row = 10
            else:
                raise CalculationError(
                    "Wire diameter "
                    + str(self.wireDiameter_in)
                    + " out of range for material "
                    + self.material
                )

        else:
            raise CalculationError("Invalid material: " + self.material)

        # now we know row, get the properties
        table10_4_props = propTable10_4[row, :]

        A = float(table10_4_props[3])
        m = float(table10_4_props[0])
        # UTS actually established
        uts_kpsi = A * self.wireDiameter_in ** (-1 * m)  # A/d**m

        # Result
        self.uts_psi = uts_kpsi * 1000

        if testing:
            return row

    # def getG(self, test=False):
    #     """Gets shear modulus G from table"""

    #     #Shigley 10-5: "ASTM Code", % tensile, % torsion, d_min [in], d_max [in], E [Mpsi], G [Mpsi]
    #     propTable10_5 = np.array(
    #         [
    #             # A228
    #             [0.65,  0.45,   0,      0.032,  29.5,   12],    #0
    #             [0.65,  0.45,   0.032,  0.063,  29,     11.85], #1
    #             [0.65,  0.45,   0.063,  0.125,  28.5,   11.75], #2
    #             [0.65,  0.45,   0.125,  1, 28,  11.6],          #3

    #             # A227
    #             [0.6,   0.45,   0.,     0.032,  28.8,   11.7],  #4
    #             [0.6,   0.45,   0.032,  0.063,  28.7,   11.6],  #5
    #             [0.6,   0.45,   0.063,  0.125,  28.6,   11.5],  #6
    #             [0.6,   0.45,   0.125,  1.,     28.5,   11.4],  #7

    #             # A232
    #             [0.88,  0.65,   0.,     1.,     29.5,   11.2],  #8

    #             # A401
    #             [0.85,  0.45,   0.,     1.,     29.5,   11.2],  #9

    #             # A313
    #             [0.65,  0.45,   0.,     1,      28.,    10.],    #10

    #             # B159
    #             [0.75,  0.45,   0.,     1.,     15.,    6.],     #11
    #         ],
    #         dtype=float
    #     )

    #     row = None

    #     if self.material == 'A228':
    #         # check based on wire diameter
    #         if (self.wireDiameter_in < propTable10_5[0,3]):
    #             row = 0
    #         elif (propTable10_5[1,2] <= self.wireDiameter_in < propTable10_5[1,3]):
    #             row = 1
    #         elif (propTable10_5[2,2] <= self.wireDiameter_in < propTable10_5[2,3]):
    #             row = 2
    #         else: # should be greater than 0.125 at this point
    #             row = 3

    #     elif self.material == 'A227':
    #         # check based on wire diameter
    #         if (self.wireDiameter_in < propTable10_5[4,3]):
    #             row = 4
    #         elif (propTable10_5[5,2] <= self.wireDiameter_in < propTable10_5[5,3]):
    #             row = 5
    #         elif (propTable10_5[6,2] <= self.wireDiameter_in < propTable10_5[6,3]):
    #             row = 6
    #         else: # should be greater than 0.125 at this point
    #             row = 7

    #     elif self.material == 'A232':
    #         row = 8

    #     elif self.material == 'A401':
    #         row = 9

    #     elif self.material == 'A313':
    #         row = 10

    #     elif self.material == 'B159':

    #     else:
    #         raise CalculationError("")

    def getG(self):
        def getA228(self):
            if self.wireDiameter_in < 0.032:
                return 12.0
            elif 0.032 <= self.wireDiameter_in < 0.063:
                return 11.85
            elif 0.063 <= self.wireDiameter_in < 0.125:
                return 11.75
            else:  # should be greater than 0.125 at this point
                return 11.6

        def getA227(self):
            # check based on wire diameter
            if self.wireDiameter_in < 0.032:
                return 11.7
            elif 0.032 <= self.wireDiameter_in < 0.063:
                return 11.6
            elif 0.063 <= self.wireDiameter_in < 0.125:
                return 11.5
            else:  # should be greater than 0.125 at this point
                return 11.4

        tableDict = {
            "A228": getA228(self),
            "A227": getA227(self),
            "A232": 11.2,
            "A401": 11.2,
            "A313": 10.0,
            "B159": 6.0,
        }

        try:
            self.G_Mlbf_in2 = tableDict[self.material]
        except KeyError:
            raise CalculationError("Invalid material: " + self.material)

    def calcMeanDiam(self):
        """Simple calculation for mean diameter"""

        self.meanDiam_in = self.OD_in - self.wireDiameter_in

    def calcSpringRate(self):
        """Calculate the spring rate"""

        C_ = self.meanDiam_in / self.wireDiameter_in

        self.kB_ = (4 * C_ + 2) / (4 * C_ - 3)

        self.k_lbf_in = (
            self.wireDiameter_in**4
            * (self.G_Mlbf_in2 * 1e6)
            / (8 * self.meanDiam_in**3 * self.na_)
        )

    def calc_sSY(self):
        """Calculates shear related stuff"""

        lookupDict = {
            "A228": 0.45 * self.uts_psi,
            "A227": 0.45 * self.uts_psi,
            "A313": 0.35 * self.uts_psi,
            "A401": 0.35 * self.uts_psi,
            "A232": 0.35 * self.uts_psi,
            "B159": 0.35 * self.uts_psi,
        }

        try:
            self.sSY_psi = lookupDict[self.material]
        except KeyError:
            raise CalculationError("Invalid material: " + self.material)

    def calcShutVals(self):
        """Calculate the spring shut force and factor safety"""

        self.fShut_lbf = self.k_lbf_in * (self.L0_in - self.Ls_in)

        tauS_lbf_in2 = (
            self.kB_
            * 8
            * self.fShut_lbf
            * self.meanDiam_in
            / (np.pi * self.wireDiameter_in**3)
        )

        self.nShut_ = self.sSY_psi / tauS_lbf_in2  # __________ OUTPUT __________
