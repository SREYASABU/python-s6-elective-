n=int(input("Enter number: "))
n1=n
rev=""
sum=0
while n!=0:
    i=n%10
    n=n//10
    sum=sum+i
    i=str(i)
    rev+=i
print(f'Sum of digits of {n1} is {sum}\nReverse of {n1} is {rev}')