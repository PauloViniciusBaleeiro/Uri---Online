# numbers = input().split()

# a = int(numbers[0])

# soma = 0

# for 
# while n <= 0:
#   n = int(input())

# while count < n:
#   soma = sum(soma, count)
#   count  = count + 1

# print(soma)
  

# def sum (sum, number):
#   return sum + number

'''
ESSA SOUÇÃO NÃO É MINHA. EU NÃO ENTENDI O PROBLEMA DIREITO
'''

x = list(map(int, input().split()))
i = 1
s = 0

while x[i] <= 0:
    if x[i] <=0:
        i = i + 1
    if x[i] > 0:
        break

for c in range(0,x[i]):
    s = s + x[0] + c
   
print(s)
