import random

# start game

def game():
    print("Rock!!---Paper!!---Scissors!!\n".ljust(59, '='))
    user = input("'r' for rock, 'p' for paper, 's' for scissors: \n")
    computer = random.choice(["r","p","s"])

    if user == computer:
        return "its a tie!!"
   
    def win(player,opponent):
        if(player == 'r' and opponent == 's') or (player == 's' and opponent == 'p') or (player == 'p' and opponent == 'r'):
            return True
        if win(user,computer):
            
            return "you won!!"
        
    return "you lost!! :("

# print()
while True:

    print(game())
    

    
  