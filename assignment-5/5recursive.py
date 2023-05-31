def factorial(n):
    if n==1:
      return 1
    else:
       return n*factorial(n-1)


n=int(input(f'Enter n of nCr:'))
r=int(input(f'Enter r of nCr:'))
i=n-r
nCr=factorial(n)/(factorial(r)*factorial(i))
print(f'nCr: {nCr}')