#here key=3
import string
n=input("Enter the string to be encrypted: ")
n1=string.ascii_lowercase
n2=string.ascii_uppercase
j=0
e=""
for i in n:
    if i.islower():
        index=n1.find(i)
        e+=n1[index+3]
    else:
        index=n2.find(i)
        e+=n2[index+3]
    j+1
print(f'Encrypted string is: {e}')