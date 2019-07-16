n1 = int(input())
n2 = int(input())

if (n1 > n2) :
    n = n2
    n2 = n1
    n1 = n
odd = 0
for x in range(n1, n2):
    if x > n1 and (x < n2) and ((x % 2) != 0):
        odd = odd + x

print (odd)