# Створити клас, конструктор якого генерує масив чисел цілого типу.
# Розмір масиву задається параметром конструктора.
# Деструктор звільняє пам’ять, що виділена під масив.
# Створити функцію, параметром якої є створений клас.
# Функція виконує дії над масивом певного типу відповідно варіанту.
# Кількість елементів: 9
# Вираз для обчислення елемента масиву: парного - і-2, непарного - і+5.
class Gen:

    def __init__(self, size=9):
        self.size = size
        self.massive = []
        for i in range(self.size):
            if i % 2 == 0:
                self.massive.append(i - 2)
            else:
                self.massive.append(i + 5)

    def __del__(self):
        return None


def main(obj):
    summ = 0
    for i in range(len(obj.massive)):
        if i % 2 != 0:
            summ += obj.massive[i]
    print(f"Сумма непарних елементів об'єкту классу, конструктор якого генерує масив чисел цілого типу дорівнює: "
          f"{summ}")


if __name__ == '__main__':
    generator = Gen()
    main(generator)
