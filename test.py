import unittest
from dial_permute_depth import DialPermute as DPD
from dial_permute import DialPermute as DP

class HorseOnAPadTestsDEPTH(unittest.TestCase):
    def test_zero_length(self):
        N = DPD().get_permutations(N=0, start=9)
        self.assertEqual(N, 0)

    def test_start_five(self):
        N = DPD().get_permutations(N=3, start=5)
        self.assertEqual(N, 0)

    def test_start_0(self):
        N = DPD().get_permutations(N=2, start=0)
        self.assertEqual(N, 2)

    def test_start_4_len_2(self):
        N = DPD().get_permutations(N=2, start=4)
        self.assertEqual(N, 3)
    
    def test_start_4_len_3(self):
        N = DPD().get_permutations(N=3, start=4)
        self.assertEqual(N, 5)


if __name__ == '__main__':
    unittest.main()