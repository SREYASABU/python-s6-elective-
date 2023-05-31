name=["Riya","Sreya","Lousie","Anna",]
rno=[69,64,4,5]
L=list(zip(rno,name))
Lname=sorted(L,key=lambda x:x[1])
Lrno=sorted(L,key=lambda x:x[0])
print(f'List: {L}')
print(f'acc. to name sort:',Lname)
print(f'acc. to rno sort:',Lrno)