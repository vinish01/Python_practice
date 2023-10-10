#list[]:
"""  *list can be mutable
     * list allows duplicates values
     * list allows all the items and any type of data can be stored"""
# a = [1, 2, 3, 4, 5]
# b = [7, 8, 9, 10]
# a.insert(1, 2)
# a.append(6)
# a.append(True)
# a.append('vin')
# a.pop(1)
# a.extend(b)
# print(a)

#Tuple():
"""* tuples are immutable
   * tuple allows duplicates values
   * tuples doesn't able to modify the items and cannot able to add or remove
   * any types of data can be stored"""

# a = (1, 2, 3, 4, 5)
# b = (7, 8, 9, 10)
#
# print(type(a))


#set{}:
"""* set are unordered
   * set doesn't allows duplicates values
   * set doesn't able to modify the items
   * set able to add or remove items"""

# a = {1, 2, 3, 4, 5}
# a.add(6)
# a.update()
# a.pop(0)
# a.remove(0)
# print(a)


#dictionary:
"""* do not allows duplicate
   * duplicate values overwrite existing values
   * any types can be stored"""

a = {
    "name": "s1",
    "age": 1,
    "dept": "data"
}
a["designation"]:"associate"
print(a)
print(a.keys())
print(a.values())