#Python collection (List)
pylist = ["go", "went", "gone", "Hello", "Python"]
print(pylist) #print the all item in the list
print(pylist[2]) #access item by referring to the index number

#Change specified Item value, refer to the index number
pylist = ["go", "went", "gone", "Hello", "Python"]
pylist[1] = "george"
print(pylist)

#Loop through a list
pylist = ["go", "went", "gone", "Hello", "Python"]
for i in pylist:
	print(i)

#Check if item exists
pylist = ["go", "went", "gone", "Hello", "Python"]
if "Hello" in pylist:
	print("Yes, it is in the list")

#Find length of the list
pylist = ["go", "went", "gone", "Hello", "Python"]
print(len(pylist)) #Use len() method to show how many item in the list
 
#Add item to the end of the list
pylist = ["go", "went", "gone", "Hello", "Python"]
pylist.append("Hacker")#use append() method
print(pylist)
#Add item at the specified index
pylist.insert(3, "one")
print(pylist)

#Remove item from the list
pylist = ["go", "went", "gone", "Hello", "Python"]
pylist.remove("gone") #remove specified index
print(pylist)
pylist.pop()# remove last item if index isn't specified
print(pylist)
del pylist[0]# remove specified index
print(pylist)

#Delete the list completely
pylist = ["go", "went", "gone", "Hello", "Python"]
del pylist

#USe list constructor to make a list
pylist = list(("Good", "Bye", "See", "You"))
print(pylist)

#Clear() empty the list
pylist = ["go", "went", "gone", "Hello", "Python"]
pylist.Clear()
print(pylist)

