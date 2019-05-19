num1 = input()
num2 = input()
num3 = input()
num4 = input()
num5 = input()
num6 = input()

numbers = []
numbers.append(num1)
numbers.append(num2)
numbers.append(num3)
numbers.append(num4)
numbers.append(num5)
numbers.append(num6)

positives = 0

for i in range(6):
    if (float(numbers[i]) > 0):
        positives += 1

print(str(positives) + " valores positivos")
