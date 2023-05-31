def sum(n):
    d=n%10
    if n==0:
        return 0
    else:
        return d+sum(n//10)
print(sum(234))