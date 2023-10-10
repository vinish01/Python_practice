# for i in range(1, 11):
#     table = i * 3
#     print(i, "* 3 =", table)
#
# a = int(input("enter a no: "))
# b = int(input("enter a no: "))
# for i in range(a, b+1):
#     print(i)


# for i in range(1, 11):
#     if i % 2 == 0:
#         print(i)

# count = 0
# for i in range(1, 11):
#     if i % 2 == 0:
#         count = count + 1
# print(count)


# count1 = 0
# count2 = 0
# for i in range(1, 10):
#     if i % 2 == 0:
#         count1 = count1 + 1
#     else:
#         count2 = count2 + 1
# print(f"Even count: {count1}")
# print(f"Odd Count: {count2}")


# count = 0
# for i in range(1, 100):
#     if i % 3 == 0 and i % 5 == 0:
#         count = count + 1
# print(count)


# list1 = []
# for i in range(1, 6):
#     list1.append(i)
# print(sum(list1))

# list2 = []
# for i in range(4):
#     a = int(input("enter a no: "))
#     list2.append(i)
# sum = sum(list2)
# avg = sum / len(list2)
# print(f"sum is {sum}")
# print(f"average is {avg}")


# n = []
# for i in range(1, 7+1):
#     n.append(i)
# sum = sum(n)
# print(sum)
# print(f"the first 7 natural no: {n}")


# a = []
# for i in range(5):
#     n = int(input("enter a no: "))
#     a.append(n)
#
# for i in a:
#     b = (i * i * i)
#     print(f"the number is: {i} and the cube is: {b}")


# for i in range(0, 5):
#     for j in range(0, i+1):
#         print('* ', end='')
#     print()


n = 5
fact = 1
for i in range(1, n+1):
    fact = fact * i

print(fact)