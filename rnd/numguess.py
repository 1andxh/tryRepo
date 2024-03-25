import random
top_of_range = input("type a number: ")

if top_of_range.isdigit:
    top_of_range = int(top_of_range)

    if top_of_range <= 0:
        print('please type a number greater than 0')
        quit()
else:
    print("please type a number")
    quit()

random_num = random.randrange(0,top_of_range)

while True:
    user_guess = input("make a guess: ")
    if random_num == user_guess.isdigit():
        user_guess = int(user_guess)
    break

