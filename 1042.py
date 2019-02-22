numbers = input().split()
valores = [int(n) for n in numbers]

valores.sort()

print(*valores, sep='\n')
print()
print(*numbers, sep='\n')