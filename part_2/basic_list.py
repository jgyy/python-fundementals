# an existing list of numbers hidden in the hat
hat_list = [1, 2, 3, 4, 5]

# ex. 1: write a line of code that prompts the user
# to replace the middle number with an integer number entered by the user
hat_list[2] = int(input("Enter a number: "))

# ex. 2: write a line of code here that removes the last element from the list
del hat_list[-1]

# ex. 3: write a line of code here that prints the length of the existing list
print(len(hat_list))

# printing the list and testing the code
print(hat_list)
print((hat_list[2] + 7) == sum(hat_list))
