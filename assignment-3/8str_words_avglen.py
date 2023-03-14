str=input("Enter the string: ")
words=str.split(" ")
sum=0
avg=0.0
count=0
for w in words:
    sum+=len(w)
    count+=1
avg=sum/count
print(f'average: {avg}')