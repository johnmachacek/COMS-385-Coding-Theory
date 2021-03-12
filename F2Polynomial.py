# exec(open("F2Polynomial.py").read())
# Need to reset the p data member to private by using __.

class F2Polynomial:
    # A class to handle F2 polynomial generation. An F2 polynomial is a list of either 1 or 0.
    # It can be thought of as any number mod(%) by 2.

    def __init__(self, p):
        if type(p) is int:
            self.__p = p

        # Need to flip the passed in list around. Its reading binary backwards right now
        elif type(p) is list:
            # Calculate the value of a binary list, as an int.

            self.__p = 0    # Generate data member p. This will be an int representing the binary number
            for i in p:     # Loop through the passed in list, and calculate the int representation
                if p[i] == 1:
                    self.__p = pow(2, i) + self.__p

                if p[i] > 1 or p[i] < 0:
                    raise ValueError("A list must contain all 1s and 0s, since it is meant to represent a binary num")
            print(self.__p)

        # Not done
        elif type(p) is str:
            # Calculate the value of a binary list, as an int.

            self.__p = 0    # Generate data member p. This will be an int representing the binary number
            for i in p:     # Loop through the passed in list, and calculate the int representation
                if p[i] == 1:
                    self.__p = pow(2, i) + self.__p

                if p[i] > 1 or p[i] < 0:
                    raise ValueError("A list must contain all 1s and 0s, since it is meant to represent a binary num")

