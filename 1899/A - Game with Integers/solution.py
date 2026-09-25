n=int(input())
lst=[]
for i in range(n):
    lst.append(int(input()))
for i in lst:
        print("Second") if i%3==0 else print("First")