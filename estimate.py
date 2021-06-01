import math
import unittest
import random
class TestWallis(unittest.TestCase):
    def test_low_iters(self):
        for i in range(0, 5):
            pi = wallis(i)
            self.assertTrue(abs(pi - math.pi) > 0.15, msg=f"Estimate with just {i} iterations is {pi} which is too accurate.\n")
            
    def test_high_iters(self):
        for i in range(500, 600):
            pi = wallis(i)
            self.assertTrue(abs(pi - math.pi) < 0.01, msg=f"Estimate with even {i} iterations is {pi} which is not accurate enough.\n")


class TestMC(unittest.TestCase):
    def test_randomness(self):
        pi0 = monte_carlo(15000)
        pi1 = monte_carlo(15000)
        
        self.assertNotEqual(pi0, pi1, "Two different estimates for PI are exactly the same. This is almost impossible.")

        self.assertFalse(abs(pi0 - pi1) > 0.05, "Two different estimates of PI are too different. This should not happen")

    def test_accuracy(self):
        for i in range(500, 600):
            pi = monte_carlo(i)
            self.assertTrue(abs(pi - math.pi) < 0.4, msg=f"Estimate with even {i} iterations is {pi} which is not accurate enough.\n")
        
    
if __name__ == "__main__":
    unittest.main()
    
import random
def monte_carlo(n) :
    ins=0
    out=0
    tot=0
    while n>0 : 
        x=random.random()
        y=random.random()
        if x**2+y**2 >1 :
            out = out+1
        else :
            ins=ins+1
            tot=ins+out
            ret=4*ins/tot
        n=n-1
    ret=(4*ins)/tot
    return ret



def wallis(i) :
    prod=1  
    n=1
    while n <= i:
        prod=prod*(4*n*n)/(4*n*n-1)
        n=n+1
    retu=prod*2
    return retu

  
        
        
        
        
       
        
        
