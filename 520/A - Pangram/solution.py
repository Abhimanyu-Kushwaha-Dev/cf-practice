n = int(input())
s = input().lower()
print("YES" if n >= 26 and len(set(s) & set("abcdefghijklmnopqrstuvwxyz")) == 26 else "NO")