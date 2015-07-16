ten_things = "apples oranges crows telephone light sugar"

stuff = ten_things.split(' ')
more_stuff = ["days", "night", "song", "frisbee", "corn", "banana", "girl", "boy"]

while len(stuff) != 10:
    next_one = more_stuff.pop()  # 默认抛出最后一个元素
    print("adding:", next_one)
    stuff.append(next_one)
    stuff_num = len(stuff)
    print("There's {} items now".format(stuff_num))

print("stuff:", stuff)
print(stuff[1])
print(stuff[-1])  # 负索引，stuff[-1]即是倒数第一个元素
print(stuff.pop())

print(' '.join(stuff))  # 用' '连接stuff，相当于join(' ', stuff)
# 用'#'连接stuff中索引从0到4的元素，即第1到5个元素
# stuff[0:5]和range(0,5)差不多，包含头，不包含尾
print('#'.join(stuff[0:5]))
