
#Comparison operators
# Logical operators
# Decision making
# loops(for loops, while loops, range, enumerator)
# min/max practice
# Random in python
# List comprehension


# review practice
# Append the value of current to the end of the list seconds 
# Please use the list.append() method to do that.



seconds = [1.23, 1.45, 1.02]
current = 1.11
seconds.append(current)

print(seconds)
# Remove item 1.45 from seconds.
seconds = [1.23, 1.45, 1.02, 1.11]
seconds.remove(1.45)
print(seconds)
# Remove items 1.45, 1.02, and 1.11 from seconds.
seconds = [1.23, 1.45, 1.02, 1.11]
seconds.remove(1.45)
seconds.remove(1.02)
seconds.remove(1.11)

print(seconds)
################################comparison operators#########################
#remember....
# > greater
# < less
# >= greater or equal
# <= less or equal
# == equal
# != different or not equal to


# Comparison Operators Practice  1:
# Create two variables (num1 and num2) with the following values: 36 and 17. 
#Check if num1 is greater than or equal to num2 and store the result of that comparison in a variable called my_bool

# num1=36
# num2=17 
# my_bool= num1 >= num2
# print(my_bool)


# Comparison Operators Practice  2:
# Create two variables (num1 and num2):
# Inside num1, store the result of the square root of 25
# Inside num2, store the number 5.
# Check if num1 is equal to num2 and store the result of that comparison in a variable called my_bool.
# import math 
# num1=math.sqrt(25)
# num2=5
# my_bool=num1==num2
# print(my_bool)
# # Comparison Operators Practice #3:
# # Create two variables (num1 and num2):
# num1 = 64*3
# num2 = 24*8
# # Inside num1, store the result of 64 x 3

# # Inside num2, store the result of 24 x 8

# # Check if num1 is different from num2 and store the 
# my_bool= num1 != num2
# # result of that comparison in a variable called my_bool.
# print(my_bool)



#######################comparison operators challenge#####################
# Challenge: Compare two numbers entered by the user and check if they are equal or not.
# If they are not equal, print which one is greater.
User_number1=int(input("Pick a number: "))
User_number2=int (input("Pick another number: "))

if User_number1 == User_number2 :
    print("equal")
elif User_number1 > User_number2 :
    print(str(User_number1))
elif User_number2 > User_number1 :
    print(str(User_number2))
# Prompt the user for two numbers

# Check for equality and greater number