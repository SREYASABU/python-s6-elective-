n=input("Enter number: ")
length=len(n)
n1=int(n)
sum=0
n=int(n)
while n!=0:
    i=n%10
    n=n//10
    sum+=i**length
if sum==n1:
    print(f'{n1} is an armstrong number of order {length}')
else:
    print(f'{n1} is NOT an armstrong number of order {length}')