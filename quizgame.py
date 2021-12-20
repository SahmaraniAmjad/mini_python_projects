print("Welcome to my computer quiz!")

# input ask the user to type something in the console
playing = input("Do you want to Play? ")

if playing.lower() != "yes":
    quit()

print("Okay! let's play :)")
score = 0

answer1 = input("What does CPU stand for? ")
if answer1.lower() == "central processing unit":
    print('Congrats, correct! keep it up')
    score += 1
else:
    print("Sorry, Incorrect!")

answer2 = input("What does GPU stand for? ")
if answer2.lower() == "graphics processing unit":
    print('Congrats, correct! keep it up')
    score += 1
else:
    print("Sorry, Incorrect!")

answer3 = input("What does RAM stand for? ")
if answer3.lower() == "random access memory":
    print('Congrats, correct! keep it up')
    score += 1
else:
    print("Sorry, Incorrect!")

answer4 = input("What does PCU stand for? ")
if answer4.lower() == "power supply":
    print('Congrats, correct! keep it up')
    score += 1
else:
    print("Sorry, Incorrect!")

print("You got " + str(score) + " questions correct!")
print("You got " + str((score/4) * 100) + " %.")

