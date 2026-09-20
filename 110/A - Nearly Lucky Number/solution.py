n=input().strip()
x=n.count('4')+n.count('7')
print("YES" if set(str(x))<={'4','7'} else "NO")