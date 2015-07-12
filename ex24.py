print("You\'d need to know \'bout escape with \\ that do \n newlines and \t tabs")

poem ="""
\tThe lovely world
with logic so firmly planted
cannot discern \n the needs of love
nor comprehend passion from intuition
and require an explanation
\n\twhere there is none
"""

print("**********************")
print(poem)
print("**********************")

five = 10 - 2 + 3 - 6
print("This should be five:{}".format(five))

def secret_formula(started):
    jelly_beans = started * 500
    jars = jelly_beans / 1000
    crates = jars / 100
    return jelly_beans, jars, crates

start_point = 10000
# 这里secret_formula(start_point)返回的是一个元组，打印出三个变量的值需要先解包
beans, jars, crates = secret_formula(start_point)

print("With a staring point of：{}".format(start_point))
print("We'd have {} beans, {} jars, {} crates".format(beans, jars, crates))

start_point = start_point / 10
print("We can also do that this way")
beans, jars, crates = secret_formula(start_point)
print("We'd have {} beans, {} jars, {} crates".format(beans, jars, crates))
