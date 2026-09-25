n=input()
if len(n)==1 or n[1:].isupper():
    print(n.swapcase())
else:
    print(n)