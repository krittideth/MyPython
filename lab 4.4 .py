a = {1,2,3,4,5,6,8}
b = {1,3,5,6,7,8}
c = {6,8,9,10}
print(a.union(b))
print(a | b | c)
print(a.intersection(b).intersection(c))
print(a & b & c)
print(b.difference(a))
print(b-a)