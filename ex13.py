from sys import argv

script, one, two, there = argv  # 用户执行命令时输入
four = input("The forth:")  # 脚本运行过程中需要用户输入

print("The script:", script)
print("The first:", one)
print("The second：", two)
print("The third:", there)
print("The forth:", four)
