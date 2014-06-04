# float
x = input("x: ")
y = input("y: ")
sf = float(x) + float(y)
print("float:",x,"+",y,"=",sf)

# int
si = int(x) + int(y)
print("int:",x,"+",y,"=",si)

# complex
sc = complex(x) + complex(y)
print("complex:",x,"+",y,"=",sc)

# boolean
sb = bool(int(x)) & bool(int(y))
print("boolean:",bool(int(x)),"&",bool(int(y)),"=",sb)

# dict
d = dict([(x,'a'),(y,'b')])
print(d)

# list
l = list("Huy")
print(l)

# tuple
t = tuple("***")
print(t)
