from datetime import date, datetime
import json

class Resume:
    def __init__(self, name="", birth_date=None, kids_ages=None, languages=None, programming_languages=None,
                 fields_of_exp=None, education=None, marital_status=None):
        self.today = date.today()
        self.name = name
        self.birth_date = birth_date
        self.marital_status = marital_status
        self.kids_ages = set()
        self.education = []
        self.fields_of_exp = fields_of_exp
        self.languages = languages
        self.programming_languages = programming_languages

    #  ---------------------- Персональна інформація ----------------------------------------------
    def calculate_age(self):
        return (self.today - self.birth_date).days // 365

    def input_pers_data(self):
        self.name = input("Введіть Ваше повне ім'я: ")
        while True:
            try:
                birth_date_input = input("Введіть дату народження у форматі дд/мм/рррр: ")
                self.birth_date = datetime.strptime(birth_date_input, "%d/%m/%Y").date()
                break
            except ValueError:
                print("Невірний формат. Спробуйте ще раз.")

        marital_status_input = input("Введіть ваш сімений статус (одруж/неодруж): ").lower()
        self.marital_status = marital_status_input if marital_status_input in ['одруж', 'неодруж'] else 'невідомо'

        kids_ages_input = input("Введіть вік Ваших дітей (якщо маєте) через пробіл: ")
        self.kids_ages = set(map(int, kids_ages_input.split()))
        print("Кількість дітей:", len(self.kids_ages))
        if any(age < 18 for age in self.kids_ages):
            print("Є неповнолітні діти.")
        else:
            print("Всі діти повнолітні.")

    #  ---------------------- Професійна інформація ----------------------------------------------
    def input_prof_data(self):
        education_input = input("Введіть Вашу професійну спеціальність (через пробіл): ")
        self.education = education_input.split()

        fields_of_exp_input = input("Введіть сфери Вашого професійного досвіду (через пробіл): ")
        self.fields_of_exp = fields_of_exp_input.split()

        languages_input = input("Введіть мови, якими Ви володієте (через пробіл): ")
        self.languages = languages_input.split()

        programming_languages_input = input("Введіть мови програмування, якими Ви володієте (через пробіл): ")
        self.programming_languages = programming_languages_input.split()


    def to_dict(self):
        return {
            "Today": self.today.strftime("%d/%m/%Y"),
            "Name": self.name,
            "Birth Date": self.birth_date.strftime("%d/%m/%Y"),
            "Age": self.calculate_age(),
            "Marital Status": self.marital_status,
            "Kids Ages": list(self.kids_ages),
            "Education": self.education,
            "Fields of Experience": self.fields_of_exp,
            "Languages": self.languages,
            "Programming Languages": self.programming_languages
        }

    def to_json(self):
        return json.dumps(self.to_dict(), indent=4)

    def to_txt(self):
        return '\n'.join([f'{key}: {value}' for key, value in self.to_dict().items()])