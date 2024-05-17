#UnitTest
import unittest

class Teste(unittest.TestCase):

    def test_A(vl1 = 1, vl2 = 1):
        vl1 = 1
        vl2 = 2
        assert(vl1 == vl2)

    def test_B(vl1 = 1, vl2 = 1):
        vl1 = 1
        vl2 = 1
        assert(vl1 == vl2)

class Teste2(unittest.TestCase):

    def test_C(vr1 = 1, vr2 = 1):
        vr1 = 1
        vr2 = 1
        assert(vr1 == vr2)