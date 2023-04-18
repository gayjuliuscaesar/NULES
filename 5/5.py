class Hexagon:
    def __init__(self, a=0):
        self.a = a

    def get_a(self):
        return self.a

    def set_a(self, a):
        self.a = a

    def area(self):
        return (3 * (3 ** 0.5) * self.a ** 2) / 2

    def __lshift__(self, other):
        print(f"Екземпляр классу {self.__class__} з довжиною сторони {self.a} та площею {self.area()}")

    def __add__(self, other):
        if not isinstance(other, (int, Hexagon)):
            raise ArithmeticError('Другий аргумент має мати тип int')

        arg = other
        if isinstance(other, Hexagon):
            arg = other.a

        return Hexagon(self.a + arg)

    def __radd__(self, other):
        return self + other


def main():
    # приклад роботи перевантажених методів __add__ та __radd__
    hex1 = Hexagon(10)
    hex2 = Hexagon(20)
    print((hex1 + 5).a, (5 + hex1).a, (hex1 + hex2).a)

    # приклад роботи перевантаженої функції __lshift__ «<<»
    hex1 << 0


if __name__ == '__main__':
    main()
