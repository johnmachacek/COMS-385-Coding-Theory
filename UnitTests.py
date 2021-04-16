import unittest
import ErrorCorrectingCode as ECC

class Test(unittest.TestCase):
    def test_0_length(self):
        print("Starting legnth test...\n")
        self.assertEqual(2,ECC.ErrorCorrectingCode(['00','11']).length())
        self.assertEqual(5,ECC.ErrorCorrectingCode(['01010','01111','01110']).length())
        self.assertRaises(ValueError,ECC.ErrorCorrectingCode,['00','001'])
        print("\nFinished with legnth test\n")


    def test_1_size(self):
        print("\nStarting size test...\n")
        self.assertEqual(2,ECC.ErrorCorrectingCode(['00','11']).size())
        self.assertEqual(6,ECC.ErrorCorrectingCode(['0011','0101','0110','1001','1010','1100']).size())
        self.assertRaises(ValueError,ECC.ErrorCorrectingCode,['000','111','000'])
        print("\nFinished with size test\n")

    def test_2_hamming_dist(self):
        print("\nStarting Hamming distance test...\n")
        self.assertEqual(3,ECC.ErrorCorrectingCode.hammingDist('000','111'))
        self.assertEqual(5,ECC.ErrorCorrectingCode.hammingDist('0000000000','0101010101'))
        print("\nFinished with Hamming distance test\n")

    def test_3_min_dist(self):
        print("\nStarting minimal distance test...\n")
        self.assertEqual(1,ECC.ErrorCorrectingCode(['00','01','10','11']).minDistance())
        self.assertEqual(3,ECC.ErrorCorrectingCode(['000000','111000','000111','111111']).minDistance())
        print("\nFinished with minimal distance test\n")

if __name__ == '__main__':
    # begin the unittest.main()
    unittest.main()
