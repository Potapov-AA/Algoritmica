class Factorial:
    def __init__(self):
        pass

    def factorial(self, number):
        if number == 1:
            return 1
        else:
            return number * Factorial.factorial(self, number - 1)
