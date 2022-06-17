set_1 = set()  # Empty set
set_2 = {}  # Dict
# print(type(set_1))

set_1 = {1, "E", 'b', 'c'}
# print(set_1)

# print(set_1[0])

# set_1.add("E")
# print(set_1)
#
# set_1.remove("E")
# print(set_1)
#
# set_1.discard("a")
# print(set_1)

# set_1.pop()
# print(set_1)
#
# set_1.clear()
# print(set_1)

# Union - Set

A = {1, 2, 3, 4}
B = {3, 4, 5, 6}

# print("Union - ")
# print(A.union(B))
#
# print("Intersection")
# print(A.intersection(B))
#
print("Difference")
print(A.difference(B))
print(B.difference(A))
