#First python programme done by Shahil Dhakal in pycharm
#Program to ask students details and store them in lists

#Asking for Data
print("Enter Your name: ")
name = input()
print("Enter your age: ")
age = input()
print("Enter your address: ")
address = input()

#storing values in list
students_data = [name,age,address]

#Printing the stored data
print("Your regestered data is: " + str(students_data))