class Engine:
    def __init__(self):
        pass

    def show(self):
        pass


class PerpEngine(Engine):
    def __init__(self):
        super().__init__()

    def show(self):
        print("Вічний двигун не існує")


class IntComEngine(Engine):
    def __init__(self, capacity, power, gas_consumption):
        super().__init__()
        self.capacity = capacity
        self.power = power
        self.gas_consumption = gas_consumption

    def show(self):
        print("Двигун внутрішнього згоряння")
        print(f"Робочий об'єм: {self.capacity} л")
        print(f"Потужність: {self.power} л.с")
        print(f"Витрата бензину на 100 км: {self.gas_consumption} л/100км")


class ElEngine(Engine):
    def __init__(self, power, voltage, phase_quantity):
        super().__init__()
        self.power = power
        self.voltage = voltage
        self.phase_quantity = phase_quantity

    def show(self):
        print("Електродвигун")
        print(f"Потужність: {self.power} кВт")
        print(f"Напруга: {self.voltage} В")
        print(f"Кількість фаз: {self.phase_quantity}")


def main():
    perp = PerpEngine()
    intcom = IntComEngine(15, 600, 8)
    elen = ElEngine(397, 400, 3)

    perp.show()
    print('\n')
    intcom.show()
    print('\n')
    elen.show()


if __name__ == '__main__':
    main()
