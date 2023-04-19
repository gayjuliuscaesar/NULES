class Item:
    def __init__(self, name: str, price: int):
        self.name = name
        self.price = price

    def get_price(self):
        return self.price

    def get_name(self):
        return self.name


class Product(Item):
    def __init__(self, name: str, price: int, quantity: int):
        super().__init__(name, price)
        self.quantity = quantity

    def get_quantity(self):
        return self.quantity

    def get_all_price(self):
        return self.price * self.quantity


class Toy(Product):
    def __init__(self, name: str, price: int, quantity: int, recommended_age: int):
        super().__init__(name, price, quantity)
        self.recommended_age = recommended_age

    def get_age(self):
        return self.recommended_age

    def play(self):
        return f"Іграшка '{self.name}' працездатна"


class DairyProduct(Product):
    def __init__(self, name: str, price: int, quantity: int, expiration_date: int):
        super().__init__(name, price, quantity)
        self.expiration_date = expiration_date

    def check_expiration_date(self, date: int):
        if int(date) > int(self.expiration_date):
            return f"{self.name} непридатне до вживання"
        else:
            return f"{self.name} придатне до вживання"


def item_check():
    it = Item('Шинка по-Київськи', 300)
    print(f"Продукт під назвою: '{it.get_name()}', коштує: {it.get_price()}грн.")
    print(f"Клас '{it.__class__}' пройшов перевірку.\n\n")


def product_check():
    pr = Product('Шинка по-Київськи', 300, 20)
    print(f"""Продукт під назвою: '{pr.get_name()}', коштує: {pr.get_price()}грн.
Кількість в наявності: {pr.get_quantity()}, загальна вартість усього продукту в наявності: {pr.get_all_price()}.""")
    print(f"Клас '{pr.__class__}' пройшов перевірку.\n\n")


def toy_check():
    to = Toy('Базз-лайтер', 100, 50, 6)
    print(f"""Продукт під назвою: '{to.get_name()}', коштує: {to.get_price()}грн.
Кількість в наявності: {to.get_quantity()}, загальна вартість усього продукту в наявності: {to.get_all_price()}.
Перевірка іграшки: {to.play()}. Рекомендований вік дитини для користування іграшкою: {to.get_age()}""")
    print(f"Клас '{to.__class__}' пройшов перевірку.\n\n")


def dairy_product_check():
    dpr = DairyProduct("Молоко", 50, 30, 27)
    print(f"""Продукт під назвою: '{dpr.get_name()}', коштує: {dpr.get_price()}грн.
Кількість в наявності: {dpr.get_quantity()}, загальна вартість усього продукту в наявності: {dpr.get_all_price()}.""")
    date = int(input('Введіть сьогоднішню дату(номер дня у місяці): '))
    print(f"Перевірка молока на придатність до вживання: {dpr.check_expiration_date(date)}")


def main():
    item_check()
    product_check()
    toy_check()
    dairy_product_check()


if __name__ == '__main__':
    main()
