def seg(arr, n):
    count = 0

    for i in range(0, n):
        if arr[i] == 0:
            count = count + 1

    for i in range(0, count):
        arr[i] = 0

    for i in range(count, n):
        arr[i] = 1
    return arr

def arr1(arr, n):
    for i in range(0, n):
        print(arr[i], end=' ')


arr = [0, 1, 0, 0, 0, 1, 0, 1, 0, 1]
n = len(arr)

print(seg(arr, n))
arr1(arr, n)



0
0
0
0
0
0
