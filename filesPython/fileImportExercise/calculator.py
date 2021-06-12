from addition import Addition


class Calculator:

    @classmethod
    def add(cls, num1, num2):
        return Addition.add(num1, num2)

    @classmethod
    def subtract(cls, num1, num2):
        return Addition.add(num1, -num2)

    @classmethod
    def multiply(cls, num1, num2):
        result = 0
        for _ in range(num2):
            result = Addition.add(result, num1)

        return result

    @classmethod
    def divide(cls, num1, num2):
        result = 0
        while num1 >= num2:
            num1 = Addition.add(num1, -num2)
            result = Addition.add(result, 1)

        return result


print(Calculator.multiply(1510, 15))
