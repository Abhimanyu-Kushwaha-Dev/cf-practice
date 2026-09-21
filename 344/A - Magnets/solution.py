n=int(input())
lst=[]
c=0
for i in range(n):
    lst.append(int(input()))
for i in range(n-1):
    if lst[i]==lst[i+1]:
        c
    else:
        c+=1
print(c+1)