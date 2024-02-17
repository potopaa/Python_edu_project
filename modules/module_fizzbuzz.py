'''
Модуль алгоритму fizzbuzz
'''


class FizzBuzzGenerator:
    def __init__(self, n):
        self.n = n

    def generate_sequence(self):
        sequence = []
        for char in range(1, self.n + 1):
            if char % 3 == 0 and char % 5 == 0:
                sequence.append("FizzBuzz")
            elif char % 3 == 0:
                sequence.append("Fizz")
            elif char % 5 == 0:
                sequence.append("Buzz")
            else:
                sequence.append(char)
        return sequence