#function to read in a user-inputted list of user's choice length, as an array to print, sort and reprint
list = []     #initialize the list

elements = int(input("Enter the number of elements you would like there to be in the list:  "))
for i in range(1, elements + 1):
  #the length of the array is set
  number = int(input("Please enter the number that fills the next place in the array (seperate entries with 'enter' key, not comma): "))
  #each element of the array the user inputs is read into the array's memory
  list.append(number)  #use append to place the values inside the array
  
#first, we will print the unsorted list
print("The unsorted list is: " , list)

#now, we will invoke the sort function
list.sort()

#now, we will print the sorted list
print("The sorted list is: ", list)
