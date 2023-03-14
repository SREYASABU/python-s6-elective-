n=int(input("Enter n(odd number): "))
i=1
n1=2
print(f'x^{i}/{i}!',end="")
i=3
while i<=n:
    if n1%2==0:
     print(f'-x^{i}/{i}!',end="")
    else:
     print(f'+x^{i}/{i}!',end="")
    n1=n1+1
    i=i+2