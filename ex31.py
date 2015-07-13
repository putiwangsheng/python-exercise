print("You enter two doors")

door = int(input("> "))
# python判断某个数处于某个值域中可以用1 < x < 10,或者x in range(1, 10)
if 1 < door < 5:
    print("You like fish or cat?")
    print("1.fish")
    print("2.cat")

    fish = int(input("> "))
    if fish in range(1, 4):
        print("the fish can de eaten by the cat")
    elif fish == 5:
        print("You can eat a fish")
    else:
        print("too many")

elif door == 0:
    print("null")

    dog = input("> ")
    if dog == "1" or dog == "2":
        print("nndjsakdj")
    else:
        print("djasdhu")

else:
    print("akdljals")
