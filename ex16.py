from sys import argv

script, filename = argv
# 写文件
fishfile = open(filename, 'w')

line = input("line:")
fishfile.write(line)

fishfile.close()

newfile = open(filename)
print("the content is:", newfile.read())
