import locale

locale.setlocale(locale.LC_ALL, 'ru_RU.UTF-8')


class Student:

    def __init__(self, name, math, ph, info):
        self.name = name
        self.math = math
        self.ph = ph
        self.info = info

    def get_ph(self):
        print(self.name + ' - ' + self.ph)


def main():
    grade = input('Введіть бал по фізиці, вибірку з якого бажали б отримати ')

    with open('data.txt', 'r', encoding='utf-8') as data:
        stud_list = []
        for line in data:
            stud = Student(*line.split())
            if line.split()[-2] == grade:
                stud_list.append(stud)

    sorted_list = sorted(stud_list, key=lambda x: x.name)

    for stud in sorted_list:
        stud.get_ph()

    print('-------------------')
    print(f'Загальна кількість учнів з оцінкою з фізики у {grade} балів: {len(stud_list)}')


if __name__ == '__main__':
    main()
