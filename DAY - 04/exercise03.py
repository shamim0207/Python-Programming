#Write a code to return True if the list’s first and last numbers are the same. If the numbers are different, return False.
def first_last_same(number_x):
    first_number=number_x[0]
    last_number=number_x[-1]
    if(first_number==last_number):
        output=True
        return output
    else:
        output=False
        return output
number_x=[10,14,20,30,15,42,58,10]
Check_same=first_last_same(number_x)
print(Check_same)