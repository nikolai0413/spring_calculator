from calculations import main, MainCalculate, CalculationError
from unittest import TestCase
from random import randint, uniform
import pytest

materialTypes = ['A228', 'A227', 'A232', 'A401', 'A313', 'B159']

endTypes = ["plain", "plainAndGround", "squaredOrClosed", "squaredAndGround"]

mainResultsKeys = ["pitch_in_rev", "nt_", "na_", "k_lbf_in", "fShut_lbf", "nShut_"]


def getMainArgs():
    return {
        "material": materialTypes[randint(0, len(materialTypes)-1)],  # random index
        "endType": endTypes[randint(0, len(endTypes)-1)],
        "wireDiameter_in": uniform(0.07, 0.25),  # random number in range
        "OD_in": uniform(10, 100),
        "L0_in": uniform(50, 400),
        "Ls_in": uniform(30, 50),
    }

def test_main():
    mainArgs = getMainArgs()
    mainReturn = main(**mainArgs)
    
    should_have = mainResultsKeys
    should_have.sort()
    does_have = list(mainReturn.keys())
    does_have.sort()

    TestCase().assertListEqual(should_have, does_have)


def test_computeEndType():
    mainArgs = getMainArgs()


    # plain
    mainArgs["endType"] = endTypes[0]
    mc = MainCalculate(**mainArgs)
    assert mc.computeEndType(True) == 0

    # plainAndGround
    mainArgs["endType"] = endTypes[1]
    mc = MainCalculate(**mainArgs)
    assert mc.computeEndType(True) == 1

    # sqauredOrClosed
    mainArgs["endType"] = endTypes[2]
    mc = MainCalculate(**mainArgs)
    assert mc.computeEndType(True) == 2
    TestCase().assertAlmostEqual(mc.nt_, mc.Ls_in / mc.wireDiameter_in - 1)    
    
    # squaredAndGround
    mainArgs["endType"] = endTypes[3]
    mc = MainCalculate(**mainArgs)
    assert mc.computeEndType(True) == 2
    TestCase().assertAlmostEqual(mc.pitch_in_rev, (mc.L0_in - 2 * mc.wireDiameter_in) / mc.na_)

    # error
    mainArgs["endType"] = endTypes[2].upper()
    mc = MainCalculate(**mainArgs)
    with pytest.raises(CalculationError):
        mc.computeEndType()



def test_computeUTS():
    """Tests logic structures in this function"""
    mainArgs = getMainArgs();
    mc = MainCalculate(**mainArgs);

    # testing logic reaches correct row
    mc.material = 'A228'
    assert mc.computeUTS(True) == 0

    mc.material = 'A227'
    assert mc.computeUTS(True) == 2

    mc.material = 'A232'
    assert mc.computeUTS(True) == 3

    mc.material = 'A401'
    assert mc.computeUTS(True) == 4

    mc.material = 'A313'
    mc.wireDiameter_in = 0.012
    with pytest.raises(CalculationError):
        mc.computeUTS()

    mc.wireDiameter_in = 0.09
    assert mc.computeUTS(True) == 5

    mc.wireDiameter_in = 0.15
    assert mc.computeUTS(True) == 6
    
    mc.wireDiameter_in = 0.30
    assert mc.computeUTS(True) == 7

    mc.wireDiameter_in = 0.45
    with pytest.raises(CalculationError):
        mc.computeUTS()

    mc.material = 'yourmom'
    with pytest.raises(CalculationError):
        mc.computeUTS()
    

def test_getG():
    mainArgs = getMainArgs();
    mc = MainCalculate(**mainArgs);

    mc.material = 'A228'
    mc.wireDiameter_in = 0.02
    mc.getG()
    assert mc.G_Mlbf_in2 == 12.0

    mc.wireDiameter_in = 0.045
    mc.getG()
    assert mc.G_Mlbf_in2 == 11.85

    mc.wireDiameter_in = 0.075
    mc.getG()
    assert mc.G_Mlbf_in2 == 11.75

    mc.wireDiameter_in = 0.126
    mc.getG()
    assert mc.G_Mlbf_in2 == 11.6

    mc.material = 'A227'
    mc.wireDiameter_in = 0.02
    mc.getG()
    assert mc.G_Mlbf_in2 == 11.7

    mc.wireDiameter_in = 0.045
    mc.getG()
    assert mc.G_Mlbf_in2 == 11.6

    mc.wireDiameter_in = 0.075
    mc.getG()
    assert mc.G_Mlbf_in2 == 11.5

    mc.wireDiameter_in = 0.126
    mc.getG()
    assert mc.G_Mlbf_in2 == 11.4

    mc.material = 'A232'
    mc.getG()
    assert mc.G_Mlbf_in2 == 11.2

    mc.material = 'A401'
    mc.getG()
    assert mc.G_Mlbf_in2 == 11.2

    mc.material = 'A313'
    mc.getG()
    assert mc.G_Mlbf_in2 == 10.

    mc.material = 'B159'
    mc.getG()
    assert mc.G_Mlbf_in2 == 6.

    mc.material = 'yourmom'
    with pytest.raises(CalculationError):
        mc.getG()

def test_calcMeanDiam():
    mainArgs = getMainArgs()
    mc = MainCalculate(**mainArgs)

    mc.calcMeanDiam()

    assert mc.meanDiam_in != None

def test_calcSpringRate():
    mainArgs = getMainArgs()
    mc = MainCalculate(**mainArgs)

    mc.computeEndType()
    mc.computeUTS()
    mc.getG()
    mc.calcMeanDiam()
    mc.calcSpringRate()

    assert mc.k_lbf_in != None