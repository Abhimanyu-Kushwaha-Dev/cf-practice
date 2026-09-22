n=int(input())
s="I hate"
for i in range(2,n+1):
    if i % 2==0:
        s+=" that I love"
    else:
        s+=" that I hate"
print(s+" it")