from .test_main import getMainArgs
from calculations import static
from random import uniform
from unittest import TestCase
import pytest


staticResultsKeys = ['nStatic_']

def getStaticArgs():
    mainArgs = getMainArgs()
    staticArgs = mainArgs
    staticArgs['Fs_lbf'] = uniform(0, 1000);
    return staticArgs
    
def test_static():
    staticArgs = getStaticArgs()
    staticResult = static(**staticArgs);


    shouldHave = staticResultsKeys
    shouldHave.sort()

    doesHave = list(staticResult.keys())
    doesHave.sort()

    TestCase().assertListEqual(shouldHave, doesHave)