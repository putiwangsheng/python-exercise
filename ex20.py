from sys import argv

script, filename = argv


def print_file(f):
    print(f.readlines())  # 返回一个列表，列表中是文件内容
    print(f.readline())  # 返回一行字符串


def read_file(f):
    f.read()


def rewind(f):
    f.seek(0)

file = open(filename)
read_file(file)
rewind(file)

print_file(file)
