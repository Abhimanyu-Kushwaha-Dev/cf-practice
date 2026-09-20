s1=input().lower()
s2=input().lower()
flag=True
diff=0
for i in range(min(len(s1),len(s2))):
    if ord(s1[i])!=ord(s2[i]):
        flag=False
        if ord(s1[i])-ord(s2[i])>=1:
            diff=1
        else:
            diff=-1
        break
if flag and len(s1)!=len(s2):
    flag=False
    diff=len(s1)-len(s2) 
print(0) if flag else print(diff)