import sys
lines = sys.stdin.read().split('
')
n = int(lines[0])
x=0
for i in lines[1:n+1]:
    if "+" in i:
        x+=1
    else:
        x-=1
print(x)