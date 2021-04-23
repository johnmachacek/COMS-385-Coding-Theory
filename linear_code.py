# Linear Code class

#CODE IS STILL IN PROGRESS

#preferred constructor pass in parity check matrix
#check each list within llist  has same length
import numpy as np
import ErrorCorrectingCode

#a = np.array([[1, 2, 3], [3, 4, 5]])
#print(a)                    #[[1 2 3]
                             #[3 4 5]]
#print(type(a))              #<class 'numpy.ndarray'>


class linear_code(ErrorCorrectingCode):

    def __init__(self, l):

#NEED TO WORK OUT HOW TO DO THIS CORRECTLY WITH NUMPY
        #Starting with only list of strings
        if type(l) is list:
            self.__l = np.ndarray(l)


    def syndrome(parity, v):

#PLACEHOLDER CODE TO WORK OUT FUNCTIONALITY
        v = "1101"
        vList = list(v)
        vMatrix = numpy.reshape(vList, (1, ))
