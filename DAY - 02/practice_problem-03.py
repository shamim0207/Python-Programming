#find the greatest of 3 numbers entered by the user
a=int (input("Enter your first number:"))
b=int (input("Enter your second number:"))
c=int (input("Enter your third number:"))
if(a>b and a>c):
    print("Your first number is greater.")
elif(b>a and b>c):
    print("Your second number is greater.")
else:
    print("Your third number is greater.")