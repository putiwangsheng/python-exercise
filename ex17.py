from sys import argv
from os.path import exists
# TODO with：

script, filename, filename2 = argv

# 将test的内容复制到test2
try:
    # 使用with无需关闭文件，也无需使用finally语句
    with open(filename, 'r') as f:
        # 判断文件是否存在
        print(exists(filename2))
        with open(filename2, 'w') as f1:
            # 将filename的内容写入filename2
            f1.write(f.read())
except:
    print("error")
