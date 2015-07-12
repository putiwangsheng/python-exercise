from sys import argv

script, filename = argv


def print_file(f):
    print(f.readlines())  # 返回一个列表，列表中是文件内容
    print(f.readline())  # 返回一行字符串,readline()里面的代码会扫面文件的每一个字节，
                         # 直到找到一个\n,停止读取文件，并返回之前读取到的文件内容。


def read_file(f):
    f.read()


def rewind(f):
    f.seek(0)

file = open(filename)
read_file(file)
rewind(file)

print_file(file)
