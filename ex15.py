from sys import argv

script, fish = argv
# 读文件 TODO 使用try except
try:
    fishtxt = open(fish)
    print(fishtxt.read())
except:
    print("error")
finally:
    if 'fishtxt' in locals():  # 检查文件中是否存在变量fishtxt
        fishtxt.close()  # 如果存在该变量，关闭文件
