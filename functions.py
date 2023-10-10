# def add():
#     a = int(input("enter a no:"))
#     b = int(input("enter a no:"))
#     print(a + b)
#
#
# add()
#
#
# def sub():
#     a = int(input("enter a no:"))
#     b = int(input("enter a no:"))
#     print(a - b)
#
#
# sub()
#
#
# def mul():
#     a = int(input("enter a no:"))
#     b = int(input("enter a no:"))
#     print(a * b)
#
#
# mul()
#
#
# def div():
#     a = int(input("enter a no:"))
#     b = int(input("enter a no:"))
#     print(a // b)
#
#
# div()


# def findevenorodd(a):
#     if a % 2 == 0:
#         print(f"{a} its is a even no")
#     else:
#         print(f"{a} its is a odd no")
#
#
# a = int(input("enter a no: "))
# findevenorodd(a)

#OR

# def findevenorodd(a):
#     if a % 2 == 0:
#         print(f"{a} its is a even no")
#     else:
#         print(f"{a} its is a odd no")
#
#
# findevenorodd(1)


# def findpassorfail(a):
#     if a > 35:
#         print("pass")
#     else:
#         print("fail")
#
#
# a = int(input("enter the mark: "))
# findpassorfail(a)


def printrange(a, b):
    for i in range(a, b):
        print(i)


a = int(input("enter a no: "))
b = int(input("enter a no: "))
printrange(a, b)