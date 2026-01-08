# calculate average
def cal_avg(numbers, n):
    total = 0
    for num in numbers:
        total = total + num
    return total / n


n = int(input("How many numbers you want to input: "))

numbers = []
for i in range(1, n + 1):
    number = int(input(f"Enter number {i}: "))
    numbers.append(number)

average = cal_avg(numbers, n)
print("Average =", average)
