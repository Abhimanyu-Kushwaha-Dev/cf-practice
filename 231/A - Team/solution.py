n=int(input())
answer=0
for i in range(n):
    bits=list(map(int,input().split()))
    answer+=(sum(bits)+3-2)//3
print(answer)