i = 0
numbers = []
step = int(input("input the step> "))

# while循环实现
while i < 6:
    print("At the top i is {}".format(i))
    numbers.append(i)

    i = i + step
    print("numbers now:", numbers)
    print("At the buttom i is {}".format(i))

# for循环实现，range（0,6 step）表示i从0到6（不包括6），step为间隔
for i in range(0, 6, step):
    numbers.append(i)

print("the numbers:")
for i in numbers:
    print(i, end=' ')

print("\n")
