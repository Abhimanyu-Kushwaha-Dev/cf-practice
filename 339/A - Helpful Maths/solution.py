s=input()
lst=[]
for i in range(0,len(s),2):
    lst.append(int(s[i]))
lst.sort()
str="+".join(str(i) for i in lst)
print(str)