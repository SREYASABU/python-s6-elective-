import math
n=int(input("Enter number: "))
n1=n
sum=0
n=int(n)
while n!=0:
    i=n%10
    n=n//10
    sum+=math.factorial(i)
if sum==n1:
    print(f'{n1} is a Krishnamurthy number')
else:
    print(f'{n1} is NOT a Krishnamurthy number')