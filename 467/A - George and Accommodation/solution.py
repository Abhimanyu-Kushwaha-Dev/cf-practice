n=int(input())
lst=[]
c=0
for i in range(n):
    lst.append(list(map(int,input().split())))
    if lst[i][1]-lst[i][0] >=2:
        c+=1
print(c)