import math

test_input = -1


def is_square(n):
    if n > 0 and math.sqrt(n) - int(math.sqrt(n)) == 0:
        return True
    else:
        return False


print(is_square(test_input))
