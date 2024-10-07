class Product:
    def __init__(self, name, quantity):
        self.name = name
        self.quantity = quantity

    def get_info(self):
        return f"{self.name} (в наличии: {self.quantity})"


class Kettlebell(Product):
    def __init__(self, name, quantity, weight):
        super().__init__(name, quantity)
        self.weight = weight

    def get_weight(self):
        return f"{self.get_info()}. Вес: {self.weight} кг"


class Clothing(Product):
    def __init__(self, name, quantity, size):
        super().__init__(name, quantity)
        self.size = size

    def get_size(self):
        return f"{self.get_info()}. Размер: {self.size}"


# Для проверки вашего кода создадим пару объектов
# и вызовем их методы:
small_kettlebell = Kettlebell('Гиря малая', 15, 2)
shirt = Clothing('Футболка', 5, 'L')

print(small_kettlebell.get_weight())
print(shirt.get_size())