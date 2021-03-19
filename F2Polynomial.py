# exec(open("F2Polynomial.py").read())
# Need to shift

class F2Polynomial:
    # A class to handle F2 polynomial generation. An F2 polynomial is a list of either 1 or 0.
    # It can be thought of as any number mod(%) by 2.

    def __init__(self, p):  # *** The convention is highest order bit on left, lowest order bit on the right. ***
        if type(p) is int:
            self.__p = p

        elif type(p) is list:
            # Calculate the value of a binary list, as a list.

            self.__p = 0    # Generate data member p. This will be an int representing the binary number
            p.reverse()     # Reverse the list that was passed in.
            for i in range(len(p)):     # Loop through the passed in list, and calculate the int representation
                if p[i] == 1:
                    self.__p = pow(2, i) + self.__p

                if p[i] > 1 or p[i] < 0:
                    raise ValueError("A list must contain all 1s and 0s (t is meant to represent a binary number)")

        elif type(p) is str:
            # Calculate the value of a binary list, as a string.

            self.__p = 0    # Generate data member p. This will be an int representing the binary number
            p = p[::-1]
            for i in range(len(p)):     # Loop through the passed in list, and calculate the int representation
                if int(p[i]) == 1:
                    self.__p = pow(2, i) + self.__p

                if int(p[i]) > 1 or int(p[i]) < 0:
                    raise ValueError("A list must contain all 1s and 0s, since it is meant to represent a binary num")
