import random
def play():
    user = input(" 'r' for rock, 'p' for paper, 's' for scissors\n")
    computer = random.choice(['r', 'p', 's'])

    if user == computer:
        return "it's a tie!!"
    

# r >s,s>p, p>r 

    
    if is_win(user, computer):
        return " you won!!!"
    
    return "lost!!"
def is_win(player, opponent):
# returnt true if player wins
    if(player =='r' and opponent =='s') or (player =='s' and opponent =='p') or (player == "p" and opponent == 'r'):
        return True
    
print(play())
