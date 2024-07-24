"""
out of the box, python offers a bunch of built-in functions to make your life as a data scientist easier. you already know two such functions: print() and type(). there are also functions like str(), int(), bool() and float() to switch between data types. these are built-in functions as well.
calling a function is easy. to get the type of 3.0 and store the output as a new variable, result, you can use the following:
result = type(3.0)
---------------------------------------------
Help!
Maybe you already know the name of a Python function, but you still have to figure out how to use it. Ironically, you have to ask for information about a function with another function: help(). In IPython specifically, you can also use ? before the function name.
To get help on the max() function, for example, you can use one of these calls:
help(max)
?max
"""
#Have a look at the documentation of sorted() by typing help(sorted) in the IPython Shell.
#You'll see that sorted() takes three arguments: iterable, key, and reverse. In this exercise, you'll only have to specify iterable and reverse, not key.
#Two lists have been created for you.
#Can you paste them together and sort them in descending order?

"""
help(sorted)
Help on built-in function sorted in module builtins:

sorted(iterable, /, *, key=None, reverse=False)
    Return a new list containing all items from the iterable in ascending order.
    
    A custom key function can be supplied to customize the sort order, and the
    reverse flag can be set to request the result in descending order.
"""

help(sorted)

# Create lists first and second
first = [11.25, 18.0, 20.0]
second = [10.75, 9.50]

# Paste together first and second: full
full = first + second

# Sort full in descending order: full_sorted
full_sorted = sorted(full, reverse=True)

# Print out full_sorted
print(full_sorted)