import getpass
import string
pwd=getpass.getpass("Enter the password: ")
c="$#@"
fl=0
fu=0
fc=0
fd=0
fe=0
if(len(pwd)>8):
        fe=1
for i in pwd:
    if(i.isupper()):
        fu=1
    if(i.islower()):
         fl=1
    if(i.isdigit):
         fd=1
    if(i in c):
         fc=1
if fe and fu and fl and fd and fc:
     print("Strong password")
else:
     print("Weak password")