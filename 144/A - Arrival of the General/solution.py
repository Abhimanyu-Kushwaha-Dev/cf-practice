n=int(input())
lst=list(map(int,input().split()))
M=lst.index(max(lst))
m=n-1-lst[::-1].index(min(lst))
s=M+(n-1-m)
if M>m:
    s-=1
print(s)