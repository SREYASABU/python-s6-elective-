#LIST 
"""
Note:In python 
     strings,integers and tuples are immutable 
     set and list are mutable
     literals are raw data assigned to variables/constants while programming"""


"""list an extremely flexible data structure
contains elements of varying type and duplicate elements"""
l2=[10,"Sreya",2.2,3,11,10,12]

print(f'\nlists are ordered: ')
l3=[2.2,11,3,10,"Sreya"]
print(f'l2: {l2}')
print(f'l3: {l3}')
print(f'l2==l3?: {l2 is l3}')#elements of l2 and l3 same , but order different

"""list-indexing-starts with 0"""
print(f'\nlist-indexing')
print(f'l2: {l2}')
print(f'l2[3]: ',l2[3])
#negative indexing 
print(f'l2[-2]',l2[-2])#prints 2nd last element


print(f'\nlist-slicing')
print("l2[2:]:",l2[2:])
print("l2[1:4]: ",l2[1:4])
print("l2[-5:-2]: ",l2[-5:-2])#l2[2:5] same as l2[-4:-2]
print(f'l2[0:6:2] {l2[0:6:2]}')
print(f'l2[6:0:-2] {l2[6:0:-2]}')
print(f'reverse of l2: {l2[::-1]}')
print(f'l2[:] is l2?: {l2[:] is l2}')#l2[:] returns a copy of l2
#in strings s[:] returns a reference to s unlike in the case of lists 
print(f'l2[:]==l2?: {l2[:]==l2}')#== checks the equality of 2 variables
#is checks if 2 varables point to same location in memory


print(f'\nlists can be nested')
l4=["hello",["world",123],"python",10]
print(f'\nl4: {l4}')
print(f'l4[1][1]: {l4[1][1]}')



l5=[10,30,40,20,20,40]
l6=[40,50,50,20,20,60,90]

print(f'\nfunctions and operations- do not modify list')
print(f'length of l5: {len(l5)}')
print(f'max of l5: {max(l5)}')
print(f'min of l5: {min(l5)}')
print(f'sum of l5: {sum(l5)}')
l8=zip(l6,l5)
print("zip(l6,l5): ",*l8)
print(f'20 in l5?: {20 in l5}')
print(f'90 not in l5?: {90 not in l5}')
#operations can be performed directly on list variables without assigning it to a variable
print(f'80 in [90,70]?: {80 in [90,70]}')


print(f'\nfunctions,operators and keywords that modify lists:')
#print(*l) to print without brackets and commas
l6=sorted(l5)#l remains unsorted
print(f'l6=sorted(l5)-l5:{l5},l6={l6}')
l5.sort()#l gets sorted
print(f'l5.sort()-l5:{l5}')
del l5[1:3]
print(f'del l5[1:3]: {l5}')#del is a keyword
l6.insert(2,100)
l7=[]
print(f'l6.insert(2,100): {l6}')
#append increments length of list by 1 and extend increments length of list by length of iterable
l7.append([200,300])
print(f'l7.append(200): {l7}')
l7.extend([200,300])
print(f'l7.extend([200,300]): {l7}')
l7.append("Sreya")
print(f'l7.append(Sreya"): {l7}')
l7.extend("Sreya")
print(f'l7.extend("Sreya"): {l7}')
print(f'l7.pop(2):{l7.pop(2)}')#takes position as argument, returns element 
l7.remove("Sreya")#takes element as argument, does not return any value
print(f'l7.remove("Sreya"): {l7}')#removes first matching element
#list concatenated with an iterable
print(f'l5+ [90,70]: {l5+[90,70]}')#[90,70]+l5 adds 90,70 to the start of l5
print(f'[90,70]*2: {[90,70]*2}')#commutative


"""lists are mutable-elements can be changed after list creation"""
print(f'\n\nlists are mutable')
print(f'l3: {l3}')
l3[4]="Riya"
print(f'l3[4]="Riya": {l3}')
#strings are immutable,individual characters cannot be changed
l3[1:4]=[10,20,30]
print(f'l3[1:4]=[10,20,30]: {l3}')

"""lists are dynamic as its size can be varied"""



