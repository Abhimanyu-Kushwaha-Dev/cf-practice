n=int(input())
flag=False
for i in range(1,n+1):
        if all(digit in '47' for digit in str(i)):
            if n%i==0:
                flag=True
print("YES") if flag else print("NO")