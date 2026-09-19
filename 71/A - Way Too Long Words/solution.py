n = int(input())
for i in range(n):
    w = input()
    print(f"{w[0]}{len(w)-2}{w[-1]}") if len(w)>10 else print(w)