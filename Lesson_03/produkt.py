# создание класса
class Product:
    # Описание класса
    name = 'Название продукта'
    price = 345.25

    def __init__(self, name, price):
        self.name = name
        self.price = price

    # Описание класса
    name = 'Название продукта'
    price = 345.25

    def sayName(self):
        return ' в наличии', self.name

    def sayPrice(self):
        return 'по цене-', self.price

    def sayMix(self):
        return 'В наличии есть ', self.name, 'по цене ', self.price
