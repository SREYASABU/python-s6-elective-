def prime(n):
    flag=0
    for x in range(2,n//2):
        if n%x==0:
            flag=1
    if flag==1:
     return False
    else :
     return True
    
L=[x for x in range(1,100) if prime(x)]
print(L)
