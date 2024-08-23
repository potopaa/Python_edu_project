# ---------------------------------------------------------------
"""

Виконав: Андрій Потопа

1. Cтворити проект python будь-яким способом, що реалізує архітектуру програмного скрипта одного з блоків структурної
схеми за власним вибором.
2. Створити віртуальне середовище віртуальне середовище - Virtual Environment.
після створення venv змінити посилання інтерпретатора на створений venv;
сформуйте властивості у файлі requirements.txt;
встановіть пакет із файлу requirements.txt.
архів проекту надайте на перевірку, шляхом завантаження його до власної директорії google drive курсу.

Package                      Version
---------------------------- -----------
pip                          24.0
DateTime                     5.4
pillow                       10.2.0

"""

from modules.module_2d import TrapezoidCalculator
import modules.module_cv as cv
from modules.module_fizzbuzz import FizzBuzzGenerator
from package_images import Im_PIL


# ---------------------- class розрахунку площі 2D-фігури -------------------------------
class TrapezoidArea:
    def __init__(self):
        self.trapezoid_calculator = TrapezoidCalculator(*TrapezoidCalculator.input_parameters())

    def trapezoid_area_calculation(self):
        area = self.trapezoid_calculator.calc_area()
        print(f"Площа трапеції, см. кв. - S: {area}")
        input("Для продовження натисніть Enter\n")


# ---------------------- class генерації FizzBuzz послідовності -------------------------


class FizzBuzSequence:
    def __init__(self):
        pass

    def fizzbuzz_sequence_generation(self):
        print("Формування FizzBuzz послідовності")
        n = int(input("Вкажіть кількість елементів послідовності:"))
        fizzbuzz_generator = FizzBuzzGenerator(n)
        result_sequence = fizzbuzz_generator.generate_sequence()
        print(result_sequence)
        input("Для продовження натисніть Enter\n")

    # ---------------------- class генерації CV  ---------------------------------------


class CVCreator:
    def write_cv(self):
        person = cv.Resume()
        person.input_pers_data()
        person.input_prof_data()

        file_type = input("Select file type. Enter 1 for .json and 2 for .txt:")

        if file_type == "1":
            file_extension = "json"
        elif file_type == "2":
            file_extension = "txt"
        else:
            print("Invalid file type selected. Exiting.")
            return

        file_name = f"{person.name.replace(' ', '_')}_CV.{file_extension}"
        with open(file_name, "w", encoding="UTF-8") as file:
            if file_extension == "json":
                file.write(person.to_json())
            elif file_extension == "txt":
                file.write(person.to_txt())
        input("Для продовження натисніть Enter\n")

# ---------------------- class трансформації зображень  ---------------------------------------

class ImageTransformator:
    def __init__(self, file_name_start=None):
        self.file_name_start = file_name_start
        self.file_name_stop = "stop.jpg"
        self.file_name_filter = "stop_filter.jpg"

    def process_image(self, mode):
        if mode == 0:
            Im_PIL.ImageTransformator.shades_of_gray(self.file_name_start, self.file_name_stop)
        elif mode == 1:
            Im_PIL.ImageTransformator.sepia(self.file_name_start, self.file_name_stop)
        elif mode == 2:
            Im_PIL.ImageTransformator.negative(self.file_name_start, self.file_name_stop)
        elif mode == 3:
            Im_PIL.ImageTransformator.noise(self.file_name_start, self.file_name_stop)
        elif mode == 4:
            Im_PIL.ImageTransformator.brightness_change(self.file_name_start, self.file_name_stop)
        elif mode == 5:
            Im_PIL.ImageTransformator.monochrome(self.file_name_start, self.file_name_stop)
        elif mode == 6:
            Im_PIL.ImageTransformator.contour_im(self.file_name_stop, self.file_name_filter)

    def input_file_name(self):
        return input("Введіть назву файлу для перетворення: ")

    def image_main_transform(self):
        if not self.file_name_start:
            self.file_name_start = self.input_file_name()

        print('Оберіть тип перетворення!')
        print('0 - відтінки сірого')
        print('1 - серпія')
        print('2 - негатив')
        print('3 - зашумлення')
        print('4 - зміна яскравості')
        print('5 - монохромне зображення')
        print('6 - фільтр-векторизатор')
        mode = int(input('Режим: '))

        self.process_image(mode)


# ---------------------- блок головних викликів  ---------------------------------------

if __name__ == "__main__":

    TrapezoidArea().trapezoid_area_calculation()
    FizzBuzSequence().fizzbuzz_sequence_generation()
    CVCreator().write_cv()
    ImageTransformator().image_main_transform()

'''

Результат:

Розрахунок площі трапеції
Сформуйте параметри трапеції:
Розмір першої основи, см - a: 22
Розмір другої основи, см - b: 22
Розмір висоти, см - h: 22
Площа трапеції, см. кв. - S: 484.0
Для продовження натисніть Enter

Формування FizzBuzz послідовності
Вкажіть кількість елементів послідовності:15
[1, 2, 'Fizz', 4, 'Buzz', 'Fizz', 7, 8, 'Fizz', 'Buzz', 11, 'Fizz', 13, 14, 'FizzBuzz']
Для продовження натисніть Enter

Введіть Ваше повне ім'я: Andrii Potopa
Введіть дату народження у форматі дд/мм/рррр: 09/09/1981
Введіть ваш сімений статус (одруж/неодруж): одруж
Введіть вік Ваших дітей (якщо маєте) через пробіл: 9 10
Кількість дітей: 2
Є неповнолітні діти.
Введіть Вашу професійну спеціальність (через пробіл): finance law
Введіть сфери Вашого професійного досвіду (через пробіл): banking compliance taxation legaltech fintech DeFi
Введіть мови, якими Ви володієте (через пробіл): ukrainian russian english polish
Введіть мови програмування, якими Ви володієте (через пробіл): sql python
Select file type. Enter 1 for .json and 2 for .txt:1
Для продовження натисніть Enter

Введіть назву файлу для перетворення: poligon.jpg
Оберіть тип перетворення!
0 - відтінки сірого
1 - серпія
2 - негатив
3 - зашумлення
4 - зміна яскравості
5 - монохромне зображення
6 - фільтр-векторизатор
Режим: 1
START_im red= 96 green= 93 blue= 100
------- ведіть коефіціент серпії --------------
depth:50
------- триває перетворення --------------
STOP_im red= 196 green= 146 blue= 96
------- перетворення завершене до файлу stop.jpg --------------

Введіть назву файлу для перетворення: poligon.jpg
Оберіть тип перетворення!
0 - відтінки сірого
1 - серпія
2 - негатив
3 - зашумлення
4 - зміна яскравості
5 - монохромне зображення
6 - фільтр-векторизатор
Режим: 6
START_im red= 188 green= 142 blue= 92
STOP_im red= 191 green= 194 blue= 199
------- перетворення завершене до файлу stop_filter.jpg --------------

Process finished with exit code 0



Резюме - якщо є бажання поділитись думками:


'''
