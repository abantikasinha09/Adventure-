name = input("Enter your name: ")

print("Welcome,", name, "to the Mystery Forest Adventure!")
print("Your journey begins now...")

answer = input(
    "You are standing at the entrance of a dark forest. "
    "There are two paths: left or right. Which path do you choose? "
).lower()

# LEFT PATH
if answer == "left":

    answer = input(
        "\nYou find an old wooden house. "
        "Do you enter the house or continue walking? (enter/walk): "
    ).lower()

    if answer == "enter":

        answer = input(
            "\nInside the house, you find a treasure chest. "
            "Do you open it or leave it? (open/leave): "
        ).lower()

        if answer == "open":
            print("\nYou opened the chest and found a bag full of gold!")
            print("Congratulations,", name, "YOU WIN! ")

        elif answer == "leave":
            print("\nYou leave the treasure behind.")
            print("Unfortunately, you never find your way out.")
            print("You lose! ")

        else:
            print("\nNot a valid option. You lose!")

    elif answer == "walk":

        answer = input(
            "\nYou reach a river. "
            "Do you swim across or follow the river? (swim/follow): "
        ).lower()

        if answer == "swim":
            print("You swim across safely and discover a beautiful village.")
            print("The villagers welcome you.")
            print("YOU WIN! ")

        elif answer == "follow":
            print("You follow the river for hours.")
            print("You get tired and lost in the forest.")
            print("You lose! ")

        else:
            print("Not a valid option. You lose!")

    else:
        print("Not a valid option. You lose!")


# RIGHT PATH
elif answer == "right":

    answer = input(
        "You come across an old bridge. "
        "The bridge looks dangerous. "
        "Do you cross it or go back? (cross/back): "
    ).lower()

    if answer == "cross":

        answer = input(
            "You safely cross the bridge and meet a mysterious stranger. "
            "Do you talk to them or ignore them? (talk/ignore): "
        ).lower()

        if answer == "talk":

            answer = input(
                "The stranger gives you a mysterious key. "
                "Do you take the key? (yes/no): "
            ).lower()

            if answer == "yes":
                print("The key opens a hidden door behind you.")
                print("Inside, you discover a magical treasure!")
                print("Congratulations,", name, "YOU WIN! ")

            elif answer == "no":
                print("You refuse the key.")
                print("The stranger disappears into the forest.")
                print("You lose! ")

            else:
                print("Not a valid option. You lose!")

        elif answer == "ignore":
            print("You ignore the stranger.")
            print("They disappear, taking the only map with them.")
            print("You become lost in the forest.")
            print("You lose!")

        else:
            print("\nNot a valid option. You lose!")

    elif answer == "back":
        print("You decide the bridge is too dangerous.")
        print("You return home safely, but your adventure ends.")
        print("You lose!")

    else:
        print("Not a valid option. You lose!")

else:
    print("Not a valid option. You lose!")


print("Thank you for playing,", name, "!")
print("Hope you enjoyed your adventure! ")
