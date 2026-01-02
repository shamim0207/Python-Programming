'''
You are given two variables, a and b. Your task is to print these variables in the following formats:

With space: Print a and b in a single line, separated by a space, followed by a newline.
Without newline: Print a and b separated by a space, but do not end the output with a newline.
With separator: Print a and b separated by a specified separator, followed by a newline.
Without space: Print a and b in a single line, with no spaces between them, followed by a newline.
'''

a=input("Enter your First value:")
b=input("Enter your Second value:")
separate="&"
# With space
print(a , b)
# Without newline
print(a,b,end="")
print()  # To move to the next line after the previous print
# With separator    
print(a , b , sep=separate)
# Without space
print(a,b , sep="")

