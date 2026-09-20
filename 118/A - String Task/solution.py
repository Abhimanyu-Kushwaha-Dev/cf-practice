s=input().lower()
vowel="aeiouy"
str=""
for i in range(len(s)):
    if(s[i] in vowel):
        str=str
    else:
        str=str+"."+ s[i]
print(str)