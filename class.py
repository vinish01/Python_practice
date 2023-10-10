class intro:

    def __init__(self, name, age, department):
        self.name = name
        self.age = age
        self.department = department

    def __str__(self):
        return f"I am {self.name}, {self.age} from department {self.department}"


a = intro('s1', 22, 'Data Analytics')
b = intro('yohanya', 24, 'Data Scientist')

print(a)
print(b)
