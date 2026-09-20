s=input()
ul=sum(1 for char in s if char.isupper())
ll=sum(1 for char in s if char.islower())
print(s.upper()) if ul>ll else print(s.lower())