k,n,w=map(int,input().split())
a=((w*k)*(w+1)//2)
print(a-n) if a>n else print(0)