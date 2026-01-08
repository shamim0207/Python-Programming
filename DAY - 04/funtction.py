def summation(n):
    total = 0
    for i in range(1, n + 1):
        total = total + i
    return total

n = int(input("Enter your number: "))
Final_sum = summation(n)
print("Sum =", Final_sum)
