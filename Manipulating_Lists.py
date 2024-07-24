# Create the areas list
areas = ["hallway", 11.25, "kitchen", 18.0, "living room", 20.0, "bedroom", 10.75, "bathroom", 9.50]

# Correct the bathroom area
areas[-1]=10.50

# Change "living room" to "chill zone"
areas[4]="chill zone"

# If you can change elements in a list, you sure want to be able to add elements to it, right? You can use the + operator:
x = ["a", "b", "c", "d"]
y = x + ["e", "f"]

# Finally, you can also remove elements from your list. You can do this with the del statement:
x = ["a", "b", "c", "d"]
del x[1]

# Currently, the first element in the areas_copy list is changed and the areas list is printed out. If you hit the run code button you'll see that, although you've changed areas_copy, the change also takes effect in the areas list. That's because areas and areas_copy point to the same list.

# If you want to prevent changes in areas_copy from also taking effect in areas, you'll have to do a more explicit copy of the areas list with list() or by using [:]
# Create list areas
areas = [11.25, 18.0, 20.0, 10.75, 9.50]
# Create areas_copy
areas_copy = areas
# Change areas_copy
areas_copy[0] = 5.0
# Print areas
print(areas)

# TO AVOID THIS

# Create list areas
areas = [11.25, 18.0, 20.0, 10.75, 9.50]
# Create areas_copy
areas_copy = areas[:]
# Change areas_copy
areas_copy[0] = 5.0
# Print areas
print(areas)