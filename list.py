l1 = ['s1', 'jai', 'jai', 'yohanya', 'monkey'],
l2 = ['s1', 'jai', 'shy', 'yohanya', 'dvya']
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