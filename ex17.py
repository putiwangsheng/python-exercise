from sys import argv
from os.path import exists
# TODO with：

script, filename, filename2 = argv
# 将test的内容复制到test2
file1 = open(filename)
content = file1.read()

# 判断文件是否存在
print(exists(filename2))

file2 = open(filename2, 'w')
file2.write(content)

file1.close()
file2.close()
