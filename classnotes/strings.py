#prints words starting with l
str="Hello folks lets learn python lets"
print(f'string is : {str}\nwords starting with l:',end="")
words=str.split(" ")
for w in words:
    if w[0]=="l":
        print(f' {w} ',end="")

#print average length of words in a string 
sum=0
avg=0.0
count=0
for w in words:
    sum+=len(w)
    count+=1
avg=sum/count
print(f'\naverage: {avg}')

#to get context of a file
remove=["is","was","but","a"]
str1=input("Enter a string: ")
str2=""
word=str1.split(" ")
for w in word:
    if w not in remove:
        str2+=w+" "
print(str2)
