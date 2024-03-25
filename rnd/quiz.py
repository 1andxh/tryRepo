print("Pop Quiz!")

play = input("Do you want to play? y = yes / n = no ")
if play.lower() != "y":
    quit()
print("Okay! Let's begin")

answer = input('What does CPU stand for? ')
if answer.lower() == "central processing unit":
    print("correct!")
else:
    print('incorrect')

answer = input('What does GPU stand for? ')
if answer == "graphics processing unit":
    print("correct!")
else:
    print('incorrect')

answer = input('What does RAM stand for? ')
if answer == "random access memory":
    print("correct!")
else:
    print('incorrect')