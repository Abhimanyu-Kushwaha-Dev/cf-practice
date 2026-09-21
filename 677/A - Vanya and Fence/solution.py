n,h=map(int, input().split())
heights = list(map(int, input().split()))
c=0
for i in heights:
    if i<=h:
        c+=1
    else:
        c+=2
print(c)