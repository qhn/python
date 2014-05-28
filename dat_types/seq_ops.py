# Access element
t = ('a',2,"aaa")
print(t[1],t[2])

print("abcd"[1])
print("abcd"[-1],'abcd'[-2])

# Concatenation
print([1,2,3]+[4,5])

l1 = [6,7]
l2 = [8,9,10]
print(l1+l2)

# Multiplication
print(0*"Hello ")
print(3*"AA ")

# Get length
print(len(l1))
print(len("""1
2
3"""))

# Mutable list
l2[-1]=11
print(l2)

# Immutable Tuple and String
# "Mode"[0]="O"
# t[1] = 1

# ID of mutable and immutable
s1 = "aaa"
s2 = "aaa"
print(id(s1)," = ",id(s2))

l3 = [1,2]
l4 = [1,2]
print(id(l3)," != ",id(l4))
