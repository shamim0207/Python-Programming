'''
Docstring for DAY - 03.practice-problem5
Write a Python program to count the total number of digits in a number using a while loop.

For example, the number is 75869, so the output should be 5.
'''
number=int (input("Enter your number:"))
count=0
while number!=0:
    number=number//10
    count=count+1
print("total number of digits:",count)