name = input("Type your name: ")
print("Welcome", name, "to this adventure!")

answer = input(
    "You are on a dirt road, it has come to and end you can go or left, which road you want to choose? ").lower()

if answer == "left":
    answer = input("You come to a river, you can walk around it swim across? Type walk to walk around and swim to "
                   "swim across ")

    if answer == "walk":
        print("you walked for many miles, ran out of water and you lost the game")
    elif answer == "swim":
        print("you swim across and were eaten by an alligator")
    else:
        print("Not a valid option. You loose!")

elif answer == "right":
    answer = input("You come into a land of magic. You want to learn magic or no")

    if answer == "yes":
        answer = input("you can learn three tricks but one of them will affect your whole life :)")

    elif answer == "no":
        print("you won the game !!!!!!")
    else:
        print("Not a valid option. You lose! ")

print("Thank you for trying", name)
