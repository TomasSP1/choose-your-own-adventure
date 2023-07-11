name = input("Type your name: ")
print("Welcome", name, "to this adventure!")

answer = input("Your are on a dirt road, it has come to an end and you can go left or right. Which way woul you like to go ? ").lower

if answer == "left":
    answer = input("You come to a river, you can walk aroud it or swim accross? Type walk to walk aroud and swim to swim accross: ").lower
    if answer == "swim":
        print("You swam to accross and were eaten by an alligator.")
    elif answer == "walk":
        print("You walked for many miles run out of water and you lost your game.")
    else:
        print("Not a valid option")

elif answer == "right":
    answer = input("You came to a bridge, ir looks wobly, do you want to cross it or head back (cross/back) ? ")
    if answer == "back":
        print("You go back and loose.")
    elif answer == "cross":
        answer = input("You crossed the bridge and met a stranger, do you talk to him (yes/now) ? ")
        if answer == "yes":
            print("You talk to the strange and you win")
        elif answer == "no":
            print("You ignored the stranger and they offended and you loose")
        else:
            print("Not a valid option")

else:
    print("Not a valid option")

print("Thank you for traying", name)


