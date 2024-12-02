class Calculator:
    def add(self, x, y):
        return x + y

    def subtract(self, x, y):
        return x - y

    def multiply(self, x, y):
        return x * y

    def divide(self, x, y):
        if y == 0:
            raise ValueError("Cannot divide by zero.")
        return x / y

if __name__ == "__main__":
    calc = Calculator()
    print("Addition:", calc.add(2, 3))
    print("Subtraction:", calc.subtract(5, 3))
    print("Multiplication:", calc.multiply(4, 2))
    try:
        print("Division:", calc.divide(10, 0))
    except ValueError as e:
        print(e)