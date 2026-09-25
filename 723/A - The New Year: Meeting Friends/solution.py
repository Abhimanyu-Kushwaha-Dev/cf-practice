lst=list(map(int,input().split()))
lst.sort()
s=lst[1]
x=0
for i in lst:
    x+=abs(i-s)
print(x)