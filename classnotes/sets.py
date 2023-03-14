#SET 
s={1,4,3,2}
#no sort() function
s1=sorted(s)#s1 is a list
print(f'\ns1=sorted(s): \ns:{s}\ns1:{s1}')
s2={10,20,30,40}
s3={30,40,50,60}
print(f'\ns2:{s2} , s3:{s3}')
print(f'max of s2: {max(s2)}\nmin of s2: {min(s2)}')
print(f'\nsum of s2:{sum(s2)}\nlength of s2: {len(s2)}')
print(f's2|s3(union): {s2|s3}')
print(f's2&s3(intersection): {s2&s3}')
print(f's2-s3(difference): {s2-s3}')
print(f's2^s3(symmetric difference): {s2^s3}')#s1-s2|s2-s1
print(f's2 subset of s3?: { s2.issubset(s3)}')
s3.add(90)
print(f'add 90 to s3: {s3}\n')

n1=int(input("enter n: "))#elements as user input
s4=set()
for i in range(n1):
    x=int(input("item:"))
    s4.add(x)
print(f's4: {s4}')
""""
not possible:
print(f'addition: {s1+s2}') 
print(f'multiply with scalar: {s1*2}')
print(s[0])
print(s[-1])
sort()(only sorted() present)"""
