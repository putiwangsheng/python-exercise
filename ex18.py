def two_fish(*ags):
    fish1, fish2 = ags
    print("fish1: {},fish2: {}".format(fish1, fish2))

def one_fish(fish1):
    print(fish1)

def no_fish():
    print("There is no fish!")

two_fish("fish1", "fish2")
one_fish("one fish")
no_fish()
