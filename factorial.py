class Factorial:
    @staticmethod
    def calculate(number):
        if number == 1:
            return 1
        else:
            return number * Factorial.factorial(number - 1)
