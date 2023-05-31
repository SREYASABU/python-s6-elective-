def binary(d):
    sum=0
    j=0
    while(d!=0):
        r=d%2
        d=d//2
        sum+=r*pow(10,j)
        j+=1
    return sum

n=int(input(f'enter the number: '))
j=0
sum=0
while(n!=0):
    d=n%10
    bin=binary(d)
    sum+=bin*pow(10,4*j)
    j+=1
    n=n//10

print(sum)

    