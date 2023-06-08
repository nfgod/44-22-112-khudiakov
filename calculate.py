# Худяков Иван Андреевич 44-22-112 вариант 26

import math
import sys


def calculate(*args):
    to_return = []

    for argument in args:
        try:
            x = float(argument)
            if x <= 0.2:
                fx = math.sqrt(x) + math.sin(x)
            else:
                fx = math.sqrt(x + math.e**x)
            to_return.append(fx)
        except Exception as e:
            print(f"Было получено исключение: {e}")
            to_return.append(None)

    return to_return


if __name__ == "__main__":
    for result, arg in zip(calculate(*sys.argv[1:]), sys.argv[1:]):
        print(f"f({arg}) = {result}")