from decimal import Decimal
class Bank:
    def __init__(self, name, value):
        self.name = name
        self.amount = Decimal(value)
        self.history = []
    def add(self, value, message):
        self.amount += Decimal(value)
        self.history.append(f"{value}: {message}.")
        print(message)
    def pay(self, price, product):
        self.amount -= Decimal(price)
        self.history.append(f"{price}: {product}.")
    def show_info(self):
        print(self.amount)
        print(self.history)

user1 = Bank("Anton", "10000")
user1.add("2499.99", "my gift for you")
user1.pay("11999.99", "Samsung galaxy S26 ultra, 512 GB")
user1.pay("499.99", "mouse")
user1.show_info()

class VeryImportant:
    def __init__(self, v1, v2):
        self.v1 = Decimal(v1)
        self.v2 = Decimal(v2)
        self.v3 = 0
    def very_important_method(self):
        self.v3 = self.v1 / self.v2
        print(self.v3)
        print(self.v3.quantize(Decimal("1.00")))
ex = VeryImportant(2, 3)
ex.very_important_method()