import sys
data=sys.stdin.buffer.read().split()
n = int(data[0])
s=0
for i in data:
    if i==b"Tetrahedron":  #i is a bytes object
        s+=4
    elif i==b"Cube":  #.decode() can also be used
        s+=6
    elif i==b"Octahedron":
        s+=8
    elif i==b"Dodecahedron":
        s+=12
    elif i==b"Icosahedron":
        s+=20
    else:
        s
print(s)