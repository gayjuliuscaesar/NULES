class Hexagon:
    def __init__(self, a=0):
        self.a = a

    def get_a(self):
        return self.a

    def set_a(self, a):
        self.a = a

    def area(self):
        return (3 * (3 ** 0.5) * self.a ** 2) / 2

    def print_info(self):
        print("Шайба зі стороною довжиною:  ", self.a)
        print("Площа шайби:  ", self.area())
