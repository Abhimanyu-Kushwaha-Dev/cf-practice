n=int(input())
lst=[]
l=[]
for i in range(n):
    lst.append(list(map(int,input().split())))
    l.append(lst[i][1]-(lst[i][0]%lst[i][1])) if lst[i][0]%lst[i][1] !=0 else l.append(0)
for i in l:
    print(i)