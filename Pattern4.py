'''
    *
   * *
  * * *
 * * * *
* * * * *
'''


n=int(input())
s = n - 1 #number of spaces
for i in range(n):
    for j in range(s):
        print(end=" ")
    s=s-1 #decrease the value for spaces
    for j in range(i+1):
        print("*",end=" ")
    print(" ")
