the_count = [1, 2, 3, 4, 5]
animals = ['fish', 'cat', 'dog', 'bird']
change = [1, 'fish', 2, 'cat', 3, 'dog']

# number在每次循环时被定义
for number in the_count:
    print("This is count {}".format(number))

for animal in animals:
    print("animal:{}".format(animal))

for i in change:
    print("I got {}".format(i))

elements = []
for i in range(0, 6):
    print("Add {} to the list".format(i))
    elements.append(i)

for i in elements:
    print("elements is {}".format(i))
