'''The int() function converts the specified value into an integer number.
We are using the same int() method to convert the given input.
int() accepts two arguments, number and base.
Base is optional and the default value is 10.
In the following program we are converting to base 17'''

num = str(input())
print(int(num,17))
'''
n=input()
print("Total len--",len(n))
for i in range(len(n)):
    if n[i]=='A':
        print(int(n[:i])+11)
    elif n[i]=='B':
        print(int(n[:i]) + 12)
    elif n[i] == 'C':
        print(int(n[:i]) + 13)
    elif n[i] == 'D':
        print(int(n[:i]) + 14)
    elif n[i] == 'E':
        print(int(n[:i]) + 15)'''
