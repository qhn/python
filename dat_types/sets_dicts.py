# Sets
m1 = {1,2,3}
m2 = set([2,2,3,3,4])
m3 = frozenset([3,4,4,5])

# Set operations
print(m1,"\n",m2,"\n",m3)
print(m1&m2)
print(m1-m2)
print(m1|m2)

# Dictionary
De2En = {"Eins":"One","Zwei":"Two","Drei":"Three"}
print(De2En["Eins"],De2En["Drei"])
