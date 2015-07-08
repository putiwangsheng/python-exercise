from sys import argv

script, use_name = argv
simble = '>>'

print("What's your name?")
name = input(simble)

print("What do you like?")
like = input(simble)

print("Your name is {} and you like {}".format(name, like))
