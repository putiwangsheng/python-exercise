from sys import argv

script, fish = argv
# 读文件 TODO 使用try except
fishtxt = open(fish)
print(fishtxt.read())

fishtxt.close()
