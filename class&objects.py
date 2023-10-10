# (self) is used to intake the object and give the result as per the object reference.


# class goa:
#     name = "empty"
#     drink = ""
#
#     def party(self):
#         print("lets drink")
#
#     def beach(self):
#         print("enjoying the beach")
#
#
# s1 = goa()
# jai = goa()
#
# s1.name = "s1"
# jai.name = "jai"
# s1.drink = "no"
# jai.drink = "yes"
#
#
# print(s1.name, "drink: ", s1.drink, s1.beach(), "\n")
# print(jai.name, "drink: ", jai.drink, jai.party())

#
# class Laptop:
#     def __init__(self):
#         self.ram = ""
#         self.processor = ""
#         self.price = 0
#
#     def hp(self):
#         return f"The hp laptop price: {self.price}, processor: {self.processor}, ram: {self.ram}\n"
#
#     def dell(self):
#         return f"The dell laptop price: {self.price}, processor: {self.processor}, ram: {self.ram}\n"
#
#     def lenovo(self):
#         return f"The lenovo laptop price: {self.price}, processor: {self.processor}, ram: {self.ram}\n"
#
#
# hp = Laptop()
# dell = Laptop()
# lenovo = Laptop()
#
# hp.price = 35000
# hp.ram = "8gb"
# hp.processor = "intel i3 12th gen"
#
# dell.price = 75000
# dell.ram = "8gb"
# dell.processor = "intel i7 12th gen"
#
# lenovo.price = 55000
# lenovo.ram = "8gb"
# lenovo.processor = "intel i5 12th gen"
#
# print(hp.hp())
# print(dell.dell())
# print(lenovo.lenovo())


# class Student:
#     def __init__(self):
#         self.name = "hi"
#         self.register_no = 1001
#
#     def display(self):
#         return f"student name is {self.name} and the register no is {self.register_no}"
#
#
# s1 = Student()
# s2 = Student()
# s1.name = "vinish"
# s1.register_no = 1813141100049
#
#
# print(s2.display())


# class Fruit:
#     def __init__(self, col, col2):
#         self.color = col
#         self.color1 = col2
#
#
# apple = Fruit("red", "black")
# print(apple.color1)


# class Teacher:
#     def __init__(self, name, register_no):
#         self.name = name
#         self.register_no = register_no
#
#     def display(self):
#         return f"Teacher name is {self.name} and the register no is {self.register_no}"
#
#
# t1 = Teacher("vinish", 101)
# t2 = Teacher("jai", 102)
#
#
# print(t1.display())
# print(t2.display())


class Calculator:
    def __init__(self, a, b):
        self.num1 = a
        self.num2 = b

    def add(self):
        return self.num1 + self.num2

    def sub(self):
        return self.num1 - self.num2

    def mul(self):
        return self.num1 * self.num2

    def div(self):
        return self.num1 // self.num2


cal = Calculator(2, 4)
print("add:", cal.add())
print("sub:", cal.sub())
print("mul:", cal.mul())
print("div:", cal.div())
