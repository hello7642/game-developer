set1={1,2,3,4,5,6,1,1,2,2,3,3,4,4,5,5,6,6}
print(type(set1))
print(set1)
#Adding elements to a list
set1.add(89)
print(set1)
set1.remove(2)
print(set1)
set2=frozenset(set1)
set2.add(17)
print(set2)