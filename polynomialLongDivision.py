#read in the user's inputted value for the polynomial
polynomialTermOne = []
polynomialTermTwo = []

#input the # of elements into the first term
n = int(input("Enter the number of elements you want the first term to have (example: 2):   "))
print("Okay, now enter the elements themselves (example: 1 2) (Seperate entries with enter key, NO COMMAS):  ")
for i in range(0, n):
  element = int(input())
  #add the element to the array using append function
  polynomialTermOne.append(element)

#input the # of elements into the second term
m = int(input("Enter the number of elements you want the second term to have. Make sure you choose MORE elements for this term, than you did for term one (example: 3):  "))
print("Okay, now enter the elements themselves (example: 1 2 3) (Seperate entries with enter key, NO COMMAS):  ")
for i in range(0, m):
  elementt = int(input())  
  #add the element to the array using append
  polynomialTermTwo.append(elementt)

#the function for the polynomial long division
while len(polynomialTermOne) <= len(polynomialTermTwo) and polynomialTermTwo:
    if polynomialTermTwo[0] == polynomialTermOne[0]:
        del polynomialTermTwo[0]    #deallocate memory
        for j in range(len(polynomialTermOne)-1): #minus one to make sure we do not go out of bounds here
            polynomialTermTwo[j] ^= polynomialTermOne[j+1]
        print(polynomialTermTwo, ": answer")
    while polynomialTermTwo and polynomialTermTwo[0] == 0:
        del polynomialTermTwo[0]    #deallocate memory
        print(polynomialTermTwo, ": remainder")
