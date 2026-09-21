n=int(input())
lst=[]
s,m=0,0
for i in range(n):
    lst.append(list(map(int,input().split())))
    s-=lst[i][0]
    s+=lst[i][1]
    if s>m:
        m=s
print(m)