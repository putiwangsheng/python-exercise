from sys import argv

script, fish = argv
# 读文件
fishtxt = open(fish)
print(fishtxt.read())

fishtxt.close()
