'''
Fibonacci Series

0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144,.....

First=0
Second=1
Third= 0+1= 1 Sum of Previous 2 values
Fourth= 1+1= 2
Fifth= 1+2= 3
Sixth= 2+3= 5
And so on....

'''
n=int(input("Enter the nth term:"))
def fibonacci(n): 
    a = 0
    b = 1
    if n < 0: 
        print("Incorrect input") 
    elif n == 1: 
        return a 
    elif n == 2: 
        return b 
    else: 
        for i in range(2,n): 
            c = a + b 
            a = b 
            b = c 
        return b 
   
  
print(fibonacci(n)) 

'''
#Python program to generate Fibonacci series until 'n' value
n = int(input("Enter the value of 'n': "))
a = 0
b = 1
sum = 0
count = 1
print("Fibonacci Series: ", end = " ")
while(count <= n):
    print(sum, end = " ")
    count += 1
    a = b
    b = sum
    sum = a + b
'''

