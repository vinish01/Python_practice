l1 = ['s1', 'jai', 'jai']
l2 = ['s1', 'vignesh', 'arun', 'jai']
l3 = []


def dif(l1, l2):
    for i in l1:
        if i not in l2:
            l3.append(i)

    for i in l2:
        if i not in l1:
            l3.append(i)

    return l3


print(dif(l1, l2))


fruits = ["apple", "banana", "cherry", "kiwi", "mango","sad"]
fruits2 = ["apple", "banana", "cherry",]
newlist = [y for y in fruits if y not in fruits2]

print(newlist)

