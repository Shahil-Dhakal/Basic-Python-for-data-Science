# To subset lists of lists, you can use the same technique as before: square brackets. This would like something like this for a list, house:
house = [["hallway", 11.25],
         ["kitchen", 18.0],
         ["living room", 20.0],
         ["bedroom", 10.75],
         ["bathroom", 9.50]
        ]
print(house[4][1])
print(house[-1][1])
print(house[4][:])