#Write Python code to iterate through the first 10 numbers and, in each iteration, print the sum of the current and previous number.
current_number=0
previous_number=0
for current_number in range(1,11):
    sum=previous_number+current_number
    print("Previous number",previous_number,"Current number",current_number,"Sum=",sum)
    current_number=current_number+1
    previous_number=sum