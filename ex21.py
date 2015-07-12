def add(a, b):
    return a + b


def substract(a, b):
    return a - b


def multiply(a, b):
    return a * b


def divide(a, b):
    return a / b

fish1 = add(10, 9)
fish2 = substract(10, 1)
fish3 = multiply(2, 3)
fish4 = divide(6, 3)
fish5 = add(fish1, multiply(fish2, divide(fish3, substract(fish4, 3))))

print("fish1:{}".format(fish1))
print("fish2:{}".format(fish2))
print("fish3:{}".format(fish3))
print("fish4:{}".format(fish4))
print("fish5:{}".format(fish5))
