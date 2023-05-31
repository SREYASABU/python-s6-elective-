L=[x for x in range(50) if x%2!=0]
cube=list(map(lambda x:pow(x,3),L))
three_divisible=list(filter(lambda x:x%3==0,L))
print(f'odd list: {L}\ncube: {cube}\nthree_divisible: {three_divisible}')