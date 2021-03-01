'''Program for Palindrome Check'''

string=input()
reverse=string[::-1]
print(reverse) 
 
if (string == reverse):
    print("Yes")
else:
    print("No")
