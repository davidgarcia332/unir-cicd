import app
import math

from app import util
class InvalidPermissions(Exception):
    pass


class Calculator:
    def add(self, x, y):
        self.check_types(x, y)
        return x + y

    def substract(self, x, y):
        self.check_types(x, y)
        return x - y

    def multiply(self, x, y):
        if not util.validate_permissions(f"{x} * {y}", "user1"):
            raise InvalidPermissions('User has no permissions')
        self.check_types(x, y)
        return x * y

    def divide(self, x, y):
        self.check_types(x, y)
        if y == 0:
            raise TypeError("Division by zero is not possible")
        return x / y

    def power(self, x, y):
        self.check_types(x, y)
        return x ** y
    def square_root(self, x):
        self.check_types(x, 0)
        if x < 0:
            return str(math.sqrt(-x)) + " * i"
        return math.sqrt(x)
    def logarithm(self, x):
        self.check_types(x, 0)
        if x <= 0:
            raise TypeError("Logarithm by less zero or zero is not possible")
        return math.log10(x)

    def check_types(self, x, y):
        if not isinstance(x, (int, float)) or not isinstance(y, (int, float)):
            raise TypeError("Parameters must be numbers")


if __name__ == "__main__":  # pragma: no cover
    calc = Calculator()
    result = calc.add(2, 2)
    print("Suma 2+2="+str(result))
    
    result = calc.substract(2, 2)
    print("Resta 2-2="+str(result))
    
    result = calc.multiply(2, 2)
    print("Multiplica 2*2="+str(result))
    
    result = calc.divide(2, 2)
    print("Division 2/2="+str(result))

    result = calc.power(2, 3)
    print("Potencia 2*3="+str(result))

    result = calc.square_root(2)
    print("Raiz cuadrada de 2 ="+str(result))

    result = calc.square_root(2)
    print("Raiz cuadrada de 2 ="+str(result))

    result = calc.logarithm(1000)
    print("Logaritmo 1000 en base 10 ="+str(result))


