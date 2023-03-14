n=float(input("Enter n:"))
n1=n
n=abs(n)
j=n
x=n
while j>0:
    x=(x+(n/x))*0.5
    j-=1
if n1<0:
 print(f'Square root of {n1} is {x}i')
else:
  print(f'Square root of {n1} is {x}')