import unittest
import numpy as np
from main import *

class UnitTests(unittest.TestCase) :
    def test_b_calculation(self) :
        for k in range(1,6) :
            for i in range(2**k) :
                num, spins = i, k*[0]
                for j in range(k) :
                    spins[k - 1 - j] = np.floor( num / 2**(k-1-j) )
                    num = num - spins[k - 1 - j]*2**(k-1-j)
                self.assertTrue( compute_b( spins )==i, "The function for calculating b does not return the correct value" )
