# exec(open("F2PolynomialVector.py").read())
import F2Polynomial

class F2PolynomialVec:

    # num is the number of integers that are generated.
    # This class generates all possible binary numbers from 0 - num^2-1
    def __init__(self, num):
        if type(num) is not int:
            raise ValueError("You must pass in an integer to this class")

        # Passed the if statement, begin function's actual work
        self.__values = [F2Polynomial(0)]     # Start the list by including 0

        for i in range(1, pow(num, 2)):
            self.__values.append(F2Polynomial(i)) # Add the i'th value into the list.

