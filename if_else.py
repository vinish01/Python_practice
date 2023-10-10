# meghna = input("Enter alive or died: ")
# if meghna == "died":
#     print("Surya meets priya")
# else:
#     print("Surya weds meghna")


# mark = int(input("enter your mark: "))
# if mark > 35:
#     print("pass")
# else:
#     print("fail")


# income = int(input("enter your income: "))
# if income > 7000:
#     print("Not eligible for scholarship")
# else:
#     print("scholarship is available")


# number = int(input("enter a no: "))
# if number % 3 == 0 and number % 5 == 0:
#     print(f"the no {number} is divisible by 3 and 5")
# else:
#     print(f"the no {number} is not divisible by 3 and 5")

# number = int(input("enter a no: "))
# if number % 2 == 0:
#     print(f"the no {number} is even")
# else:
#     print(f"the no {number} is odd")


# score = int(input("enter a score out of 100: "))
# if score < 35:
#     print(f"the score is {score} so poor student 😢")
# elif 35 < score < 70:
#     print(f"the score is {score} so average student 😁")
# elif score > 70 and score < 100:
#     print(f"the score is {score} so good student 😍")
# else:
#     print(f"enter {score} is invalid")


# a = int(input("enter a no: "))
# b = int(input("enter a no: "))
# c = input("choose either one add/sub/mul/div ")
#
# if c == "add":
#     print(f"the added value is {a+b}")
# elif c == "sub":
#     print(f"the subtract value is {a - b}")
# elif c == "mul":
#     print(f"the multiplied value is {a * b}")
# elif c == "div":
#     print(f"the divided value is {a // b}")
# else:
#     print("choose a correct option")


# score_percentage = int(input("enter a score percentage: "))
# if score_percentage > 70:
#     name = input("enter your name: ")
#     department = input("enter your department: ")
#     location = input("enter your location: ")
#     print(f"the name is {name} \nthe department is {department} \nthe location is {location}")
#     print("you are eligible")
# else:
#     print("you are not eligible")


# salary = int(input("enter the salary: "))
# age = int(input("enter the age: "))
#
# if salary >= 20000 or age <= 25:
#     loan = int(input("enter the required loan amount: "))
#     if loan <= 50000:
#         print("you are eligible for loan")
#     else:
#         print("maximum loan amount is 50,000")
# else:
#     print("you are not eligible")


sub1 = int(input("enter sub1 mark: "))
sub2 = int(input("enter sub2 mark: "))
sub3 = int(input("enter sub3 mark: "))
sub4 = int(input("enter sub4 mark: "))
sub5 = int(input("enter sub5 mark: "))
list1 = [sub1, sub2, sub3, sub4, sub5]
total = sum(list1)
average = total / len(list1)

if average > 35:
    print("Additional class needed")
else:
    print()
