'''Python program to reverse a number'''
num = int(input())
rev = 0
while num > 0:
  rem = num % 10  # Finding the remainder
  rev = (rev*10) + rem
  num = num//10  # Finding the quotient
print("%d " %rev)
