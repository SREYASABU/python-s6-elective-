n=input("Enter string:")
n.lower()
vowels = "aeiou"
consonants = "bcdfghjklmnpqrstvwxyz"
digits="0123456789"
c=0
v=0
d=0
s=0
i=0
while i<len(n):
    if n[i] in consonants:
        c+=1
    elif n[i] in vowels:
        v+=1
    elif n[i] in digits:
        d+=1
    elif n[i].isspace:
        s+=1
    i+=1
print(f'consonants: {c}\nvowels:{v}\ndigit: {d}\nspaces: {s}')