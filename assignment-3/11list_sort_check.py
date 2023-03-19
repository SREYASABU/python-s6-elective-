l=list()
n=int(input("Enter the number of elements in list: "))
for i in range(n):
    num=int(input("no:"))
    l.append(num)
print(f'list is {l}')
l1=l
if l1==sorted(l):
    print(f'list is sorted in ascending order')
elif l1==sorted(l):
    print(f'list is sorted in descending order')
else:
    print(f'list is not sorted')