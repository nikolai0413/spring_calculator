from calculations import main
from unittest import TestCase
from random import randint, uniform
import pytest

materialTypes = [
    "Music wire (ASTM No. A228)",
    "Hard-drawn wire (ASTM No. A227)",
    "Chrome-vanadium wire (ASTM No. A232)",
    "Chrome-silicon wire (ASTM No. A401)",
    "302 stainless wire (ASTM No. A313)",
    "Phosphor-bronze wire (ASTM No. B159)",
]

endTypes = ["Plain", "Plain and ground", "Squared or closed", "Squared and ground"]

mainResultsKeys = ["pitch_in_rev", "nt_", "na_", "k_lbf_in", "Fls_lbf", "n_ls_"]


def getMainArgs():
    return {
        "material": materialTypes[randint(0, len(materialTypes)-1)],  # random index
        "endType": endTypes[randint(0, len(endTypes)-1)],
        "wireDiameter_in": uniform(1, 5),  # random number in range
        "OD_in": uniform(10, 100),
        "L0_in": uniform(50, 400),
        "Ls_in": uniform(30, 50),
    }

@pytest.mark.skip
def test_main():
    mainArgs = getMainArgs()
    mainReturn = main(**mainArgs)
    
    should_have = mainResultsKeys
    should_have.sort()
    does_have = list(mainReturn.keys())
    does_have.sort()

    TestCase().assertListEqual(should_have, does_have)
