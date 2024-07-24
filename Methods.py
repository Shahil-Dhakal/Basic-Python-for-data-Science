#Strings come with a bunch of methods. Follow the instructions closely to discover some of them. If you want to discover them in more detail, you can always type help(str) in the IPython Shell.
#A string place has already been created for you to experiment with.
# string to experiment with: place
place = "poolhouse"
# Use upper() on place: place_up
place_up = place.upper()
# Print out place and place_up
print(place); print(place_up)
# Print out the number of o's in place
print(place.count('o'))

"""
ngs are not the only Python types that have methods associated with them. Lists, floats, integers and booleans are also types that come packaged with a bunch of useful methods. In this exercise, you'll be experimenting with:
.index(), to get the index of the first element of a list that matches its input and
.count(), to get the number of times an element appears in a list.
"""

# Create list areas
areas = [11.25, 18.0, 20.0, 10.75, 9.50]
# Print out the index of the element 20.0
print(areas.index(20.0))
# Print out how often 9.50 appears in areas
print(areas.count(9.50))

"""
.append(), that adds an element to the list it is called on,
.remove(), that removes the first element of a list that matches the input, and
.reverse(), that reverses the order of the elements in the list it is called on.
"""

# Create list areas
areas = [11.25, 18.0, 20.0, 10.75, 9.50]
# Use append twice to add poolhouse and garage size
areas.append(24.5); areas.append(15.45)
# Print out areas
print(areas)
# Reverse the orders of the elements in areas
areas.reverse()
# Print out areas
print(areas)