# A list is a collection if items in a particular order. you can put anything you want in a list and the items do not have to be related or of the same type. 
# Good convention is to name your lists Plural like numbers, letters, names, etc...
# Lists are created with square brackets and items seperated with commas ["apples", "pears", "banannas"]  if you print a list it prints it with the brackets.

fruits = ["apples", "pears", "banannas"] 
print(fruits)

# You can access any item in a list by its position also knows as its index starting with 0 at the forst position. To access an item you call the list name then the index in square brackets

print(fruits[1])

# Index one got the second item because we atart counting at 0.

# You can also call items from the end of a list for example index -1 will get the last item

print(fruits[-1])

# You can use string methods to properly format list elements as well. For instance you may use .title() on a user input for name to ensure cinsistency in display. 

print(fruits[1].title())
print(fruits[0].upper())

# You can use a f-string to create messages based on list elements

print(f"I love {fruits[2]} I eat them all the time")

# Most lists are dynamic meaning we will be adding or removing items as we work through a process. 
