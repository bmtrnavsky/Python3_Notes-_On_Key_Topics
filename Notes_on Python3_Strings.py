#variable.title() capitalizes every word ike a title. 
name = "ada lovelace"
print(name.title())
print(name.upper())
print(name.lower())
# .lower() is useful when saving user input data to strip all capitalization then you can run a different method to ensure it's all formated the same. 

#You can combine strings in variables to one variable then use that in a sentance with a "f" String
first_name = "ada"
last_name = "lovelace"
full_name = f"{first_name} {last_name}"
print(f"Hello {full_name.title()}")

#You can also make the entire message a variable
message = f"Hello {full_name.title()}"
print(message)

#You can add whitespace to a string with \t
print("Python")
print("\tPtyhon") 
#\n will give you a new line 
print("Languages:\nPython\nC\nJavaScript")

#You can also combine spaces and new lines with \n\t
print("Languages:\n\tPython\n\tC\n\tJavaScript")

# .strip removes extra spaceson on either side rstrip or lstrip just do one side
favorite_language = 'Python '
striped_favorite_language = favorite_language.rstrip()

#how to use an apostrophy
message = "One of Python's strengths is it's diverse community"
print(message)
#you can also use the backslash \ to ignore special charicters. 
ignore = 'One of Python\'s strengths is it\'s diverse community'
print(ignore)
