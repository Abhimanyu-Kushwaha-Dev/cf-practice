import sys
data=sys.stdin.buffer.read().split()
n=int(data[0])
names=data[1:1+n]
count={}
for i in names:
    if i not in count:
        print("OK")
        count[i]=1
    else:
        print(i.decode()+str(count[i]))
        count[i]+=1