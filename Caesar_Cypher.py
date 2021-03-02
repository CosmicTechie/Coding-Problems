'''
Ceaser Cypher :
Given
a=z 
b=y
............ z=a
For exaple.
Input: abc
Output should Be:  zyx
'''

s=input()
res=''
for i in range(len(s)):
    res=res+chr(ord('z')-ord(s[i])+ord('a'))
print(res)
