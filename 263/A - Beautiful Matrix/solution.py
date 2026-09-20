for i in range(5):
    a=list(map(int,input().split()))
    if 1 in a:
        row=i+1
        col=a.index(1)+1
print(abs(3-row)+abs(3-col))