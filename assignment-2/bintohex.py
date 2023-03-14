n=int(input("Enter 8-bit binary number: "))
count,j=0,0
sum=0
def hex(a):
    match a:
        case "10":
            a="A"
        case "11":
            a="B"
        case "12":
            a="C"
        case "13":
            a="D"
        case "14":
            a="E"
        case "15":
            a="F"
    return(a)
while n!=0:
    if count==4:
        d1=hex(str(sum))
        sum=0
        j=0
    i=n%10
    n=n//10
    sum+=i*(2**j)
    count+=1
    j+=1
d2=hex(str(sum))
hexa=d2+d1
print(hexa)