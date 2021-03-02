'''Find the difference between the sum of odd and even position digits
Example:

Input 1234
Output 2

Explanation:
sum of values at odd position: 1+3=4
sum of values at even position: 2+4=6

         6-4=2
'''

inp=input()
num=[]
for a in inp:
    a=int(a)
    num.append(a)
sumofeven,sumofodd = 0,0
for i in range(1,len(num)+1):  
    if i % 2 ==0:  
        sumofeven = sumofeven + num[i-1]
    else:
        sumofodd = sumofodd + num[i-1]
print(sumofodd,sumofeven)
print(abs(sumofodd-sumofeven))
