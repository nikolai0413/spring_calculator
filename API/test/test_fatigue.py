from API.calculations import fatigue
from unittest import TestCase
from random import randint, uniform
from .test_main import getMainArgs


fatigueResultKeys = ['n_f_']

def getFatigueArgs():
    mainArgs = getMainArgs()
    fatigueArgs = mainArgs

    fatigueArgs['F_max_N'] = uniform(300,500)
    fatigueArgs['F_min_N'] = uniform(100,300)

    return fatigueArgs

def test_fatigue():
    fatigueArgs = getFatigueArgs()
    fatigueReturn = fatigue(**fatigueArgs)

    should_have = fatigueResultKeys
    should_have.sort()
    does_have = list(fatigueReturn.keys())
    does_have.sort()

    TestCase().assertListEqual(should_have, does_have)

