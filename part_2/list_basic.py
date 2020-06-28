list = [1, 2, 4, 4, 1, 4, 2, 6, 2, 9]
newlist = []
for number in list: # browse all numbers from source list
	if number not in newlist: # if the number doesn't appear within the new list...
		newlist.append(number) # ... append it there
list = newlist[:] # make a copy of newlist
print("list with unique elements only:")
print(list)
