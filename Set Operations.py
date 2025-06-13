set1 = {1,2,3}
set2 = {2,3,4}
print(set1 | set2) #union
print(set1 & set2) #Intersection
print(set1 - set2) #Difference - only in first set
print(set1 ^ set2) #Symmetric Difference - both in two sets

#Built-in Functions
#intersection(),union(),difference(),issubset(),issuperset()
set_a = {4,6,8}
set_b = {2,4,6,8,10,12,14,16,18}
print(set_a.issubset(set_b))
print(set_b.issubset(set_a))
print(set_a.issuperset(set_a))
print(set_a.issuperset(set_b))