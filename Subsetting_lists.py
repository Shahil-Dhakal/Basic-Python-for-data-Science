# For selecting the iteams from list we use index.
list1 = [1,2,3,4,5,6,7,8,9]
print(list1[5]) #Index start from 0.

# To attain multiple items from list we use ----SLICING----
print(list1[3:5]) #This will print 3rd and 4th index. 5th wont be printed

#If you didnt specify the index while slicing, it will print the whole aftr/before.eg:
print(list1[:6])#This will print from index 0 to 5, as we know 6th index isn't printed.
print(list1[2:])#This will print whole element from 2.

print(list1[:])#Complete list is printed

# NEGATIVE INDEXING
# list1[8] and list1[-1] will give same output. The concept of negative indexing is thatit starts from end.
print(list1[8])
print(list1[-1])