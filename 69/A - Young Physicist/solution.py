n=int(input())
lst=[]
for i in range(n):
    x,y,z=map(int,input().split())
    lst.append([x,y,z])
s1,s2,s3=0,0,0
for p in lst:
    s1+=p[0]
    s2+=p[1]
    s3+=p[2]
print("YES") if s1==s2==s3==0 else print("NO")