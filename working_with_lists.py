# We can use loops for a lot of things in Python. In this example I'll print the name of a group of football players

football_players = ['elliott', 'mahomes', 'rice', 'jackson', 'saunders']
for player in football_players:
  print(player)
# You can also capitalize the names
for player in football_players:
  print(player.title())

# the way this works:
  #  For player in football players tells python look at every player in the list football players and assign it the variable player then loop through the list and complete the next set of instructions untill it has done it for every player in the lisat. In this case print the name untill it runs out of list items. 

  # you can set the temporary variable to anything you want but it is preferable to set it to something descriptive like cor cat in cats: for dog in dogs: for car in cars: for n in mumber for item in list_of_items etc. 

# You can do almost anythng with items in a list and a loop here I will capitalize the nale and create a sentance that says player scored a touchdown. 

for player in football_players:
  print(f"{player.title()} scored a touchdown!")

# You can add as many instructions inside the for loop as you want as long as you remain indented it will loop through over and over and complete all steps before moving to the next unindented instruction. I'll ad another step to the previous loop then break the loop with a thank you. 

for player in football_players:
  print(f"{player.title()} scored a touchdown!")
  print(f"I always expect {player.capitalize()} to do well, but he is playing exceptionally well today!")
print("Thank you for watching the game with me today.")
# Notice the final print statement did not loop. 
