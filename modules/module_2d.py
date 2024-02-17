'''
Модуль розрахунку площі фігури
'''


class TrapezoidCalculator:
    def __init__(self, a: float, b: float, h: float):
        self.a = a
        self.b = b
        self.h = h

    def calc_area(self) -> float:
        return (self.a + self.b) / 2 * self.h

    @staticmethod
    def input_parameters():
        print("Розрахунок площі трапеції")
        print('Сформуйте параметри трапеції:')
        a = float(input('Розмір першої основи, см - a: '))
        b = float(input('Розмір другої основи, см - b: '))
        h = float(input('Розмір висоти, см - h: '))
        return a, b, h





