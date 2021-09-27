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

# To change a element use the name of the list followed by its index

fruits[1] = "pineapple"
print(fruits)

# You can add items to the end of a list using .append

fruits.append("strawberry")
print(fruits)

# You can also start with a blank list example_lists[] then use a series of .appends to add to it. 

cars = []
cars.append("Porsche")
cars.append("Audi")
cars.append("Ford")
cars.append("Ferrari")
cars.append("Volkswagen")
print(cars)

# You can add items to any location using .insert and the index location

cars.insert(2, "BMW")
print(cars)

# Items can be permenantly removed from a list according to position using the delete statement

del cars[-1]
print(cars)

# Items can also be removed and reused with a pop statement
popped_cars = cars.pop()
print(cars)
print(popped_cars)

# Items can also be removed by value bt using the remove statement. .remove only removes the forst occurance of a word. If you need all occurances removed you would need to do a loop to get them all. 

cars.remove('Audi')
print(cars)
american_made = 'Ford'
cars.remove(american_made)
print(cars)
print(f"\n {american_made} is made in America and not Europe")

# You can permenantly sort a list with the sort method. .sort() sorts alphabetically .sort(reverse=True) sorts in reverse alphabetical order

bikes = []
bikes.append("Trek")
bikes.append("Mongoose")
bikes.append("GT")
bikes.append("Cannondale")

print(bikes)
bikes.sort()
print(bikes)
bikes.sort(reverse=True)
print(bikes)

#Sorting lists temporarily using the sorted() function
