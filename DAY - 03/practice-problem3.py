#Write a Python program to accept a number from a user and calculate the sum of all numbers from 1 to a given number
N=int(input("Enter your Number:"))
i=1
sum=0
for i in range (1,N+1)  :
    sum=sum+i
    print(sum)
    i=i+1