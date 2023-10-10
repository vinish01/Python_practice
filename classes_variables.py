class Phone:
    # class variable
    chargertype = "C-type"

    # instance variable(self)
    def __init__(self, brand, price):
        self.brand = brand
        self.price = price

    def display(self):
        return f"brand: {self.brand}, price: {self.price}, charger type:{self.chargertype}"


oppo = Phone("oppo", 10000)
print(oppo.display())
