def movea(m1, res):
    res = m1 + res[len(m1):]
    return res

print(movea(['m','o','v','e'],['m','o','v', 'a']))