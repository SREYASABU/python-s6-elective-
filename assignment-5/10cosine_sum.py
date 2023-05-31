def factorial(n):
    if n==1:
      return 1
    else:
       return n*factorial(n-1)
    
n=int(input("Enter n: "))
x=int(input("Enter x: "))
i=2
n1=2
sum=1-pow(x,i)/i
print("Sum of cosine series: ",end="")
print(f'1-{x}^{i}/{i}!',end="")
i=4
j=3
while j<=n:
    if n1%2!=0:
     print(f'-{x}^{i}/{i}!',end="")
     sum-=(x**i)/factorial(i)
    else:
     print(f'+{x}^{i}/{i}!',end="")
     sum+=(x**i)/factorial(i)
    n1=n1+1
    i=i+2
    j+=1
print(f' is {sum}')