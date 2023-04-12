class Cross:
    def __init__(self, a=0, b=0):
        self.a = a
        self.b = b

    def get_a(self):
        return self.a

    def set_a(self, a):
        self.a = a

    def get_b(self):
        return self.b

    def set_b(self, b):
        self.b = b

    def area(self):
        return self.a * self.b

    def print_sqrt(self):
        print(f"Cross with sides a = {self.a}, b = {self.b} has area={self.area()}")


def frd(cross1, cross2):
    a = cross1.get_a() + cross2.get_a()
    b = cross1.get_b() + cross2.get_b()
    frd_cross = Cross(a, b)
    return frd_cross
