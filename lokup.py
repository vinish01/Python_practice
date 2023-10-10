def lokup(items, res):
    for item in items:
        if item == res:
            return True

    return False


print(lokup(['app', 'phone', 'mac'] ,'phone'))