s1=input()
s2=input()
s=""
for i in range(len(s1)):
    if s1[i]==s2[i]:
        s+="0"
    else:
        s+="1"
print(s)