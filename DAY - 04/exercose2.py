#Write a Python code to accept a string from the user and display characters present at an even index number.
# Write a Python code to accept a string from the user
# and display characters present at an even index number.

text = input("Enter your string: ")

for i in range(0, len(text), 2):
    print(text[i])
