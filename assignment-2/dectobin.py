n=int(input("Enter decimal number: "))
binary=""
while n!=0:
    i=str(n%2)
    n=n//2
    binary+=i
print(f'Binary equivalent is: {binary[::-1]}')