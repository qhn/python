# Short string
s1 = "Python"
s2 = '123456'

print(s1,s2)
print(s1[0],s1[1],s1[2],s1[3],s1[4],s1[5])
print(s2[0],s2[1],s2[2],s2[3],s2[4],s2[5])

# Long string
s3 = """Python
is
\'good\' \\
"""
s4 = '''123
456
 789'''

print(s3)
print(s4) 

# Bytestring
b = bytes([97,98,99,100])
print(b)
b = b'abc'
print(b[0])

# Tupel
t = ("Wernerwerkdamm",5,'\n',13629,'Berlin')
print(t[0],t[1],t[2],t[3],t[4])

# List
print([])
print([1,2,3])

# Bytearray
ba = bytearray([100,101,102])
print(ba)
