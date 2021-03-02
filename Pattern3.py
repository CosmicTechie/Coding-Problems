'''
        *
      * *
    * * *
  * * * *
* * * * *
'''


n=int(input())
s = 2*n - 2 #number of spaces
for i in range(n):
    for j in range(s):
        print(end=" ")
    s=s-2 #decrease the value for spaces
    for j in range(i+1):
        print("*",end=" ")
    print(" ")
