import math
n=int(input("Enter n(even number): "))
x=int(input("Enter x: "))
i=1
n1=2
sum=0
print("Sum of sine series: ",end="")
print(f'{x}^{i}/{i}!',end="")
i=3
while i<=n:
    if n1%2==0:
     print(f'-{x}^{i}/{i}!',end="")
     sum-=(x**i)/math.factorial(i)
    else:
     print(f'+{x}^{i}/{i}!',end="")
     sum+=(x**i)/math.factorial(i)
    n1=n1+1
    i=i+2
print(f' is {sum}')