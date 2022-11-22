#s= input()
#for i in range(len(s)):
 #   if i % 2 == 1:
  #   print(s[i], end="")
#s = input()
#count = 0

#for c in s:
 #   if c.isupper():
  #      count += 1
#print(count)
#import random

#n1 = random.randint(0, 100)
#n2 = random.randint(0, 100)
#print(n1, n2)
#guess = int(input())
#if guess == n1 + n2:
   # print("True")
#elif
  #  print("False")
s = input()

for i in range(len(s)) - 1, -1, -1): #len(s)-1 to 0
      print(s[i], end="")
num = int(input())
print(num % 10, end="")
num //= 10
print(num % 10, end="")
num //= 10
print(num % 10, end="")
num //= 10