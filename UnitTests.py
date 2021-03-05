import unittest
import ErrorCorrectingCode as ECC

class Test(unittest.TestCase):
    def test_0_length(self):
        print("Starting legnth test\n")
        self.assertEqual(2,ECC.ErrorCorrectingCode(['00','11']).length())
        self.assertEqual(5,ECC.ErrorCorrectingCode(['01010','01111','01110']).length())
        self.assertRaises(ValueError,ECC.ErrorCorrectingCode,['00','001'])
        print("\nFinished with legnth test\n")

if __name__ == '__main__':
    # begin the unittest.main()
    unittest.main()
