n=input("Enter the string: ")
n1=""
for i in range(len(n)):
    if n[i].isupper():
        n1+=n[i].lower()
    else:
        n1+=n[i].upper()
print(n1)