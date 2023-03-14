n=int(input("Enter binary number: "))
sum=0
j=0
while n!=0:
    i=n%10
    n=n//10
    sum+=i*(2**j)
    j+=1
print(f'Decimal equivalent is: {sum}')