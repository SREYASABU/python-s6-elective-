n=input("Enter hex number: ")
binary=""
def convert(a):
    match a:
        case "0":
            a="0000"
        case "1":
            a="0001"
        case "2":
            a="0010"
        case "3":
            a="0011"
        case "4":
            a="0100"
        case "5":
            a="0101"       
        case "6":
            a="0110" 
        case "7":
            a="0111" 
        case "8":
            a="1000"     
        case "9":
            a="1001"   
        case "A":
            a="1010"
        case "B":
            a="1011"
        case "C":
            a="1100"
        case "D":
            a="1101"
        case "E":
            a="1110"
        case "F":
            a="1111"
    return(a)
i=0
while i<len(n):
    binary+=convert(n[i])
    i+=1
print(f'Binary equivalent is {binary}')
binary=int(binary)
sum=0
j=0
while binary!=0:
    i=binary%10
    binary//=10
    sum+=i*(2**j)
    j+=1
print(f'Decimal equivalent is: {sum}')


