#to print a number in words
n=int(input("Enter number: "))
n1=n
rev=""
sum=0
while n!=0:
    i=str(n%10)
    n=n//10
    rev+=i
rev=int(rev)
while rev!=0:
    i=rev%10
    rev//=10
    match i:
        case 0:
            print("Zero",end=" ")
        case 1:
            print("One",end=" ")
        case 2:
            print("Two",end=" ")
        case 3:
            print("Three",end=" ")
        case 4:
            print("Four",end=" ")
        case 5:
            print("Five",end=" ")
        case 6:
            print("Six",end=" ")
        case 7:
            print("Seven",end=" ")
        case 8:
            print("Eight",end=" ")
        case 9:
            print("Nine",end=" ")