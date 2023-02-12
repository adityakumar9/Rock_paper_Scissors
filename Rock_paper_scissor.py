# Make a two-player Rock-Paper-Scissors game
# Rock beats scissors
# Scissors beats paper
# Paper beats rock

import random
# player 1 taking random option
num = random.randint(1,3)
#print(num)

if num == 1:
    player1 = 'R'
elif num == 2:
    player1 = 'P'
elif num == 3:
    player1 = 'S'
else:
    "None"

player2 = input("Player 2 Turn; Chose any one: Rock(R), Paper(P), Scissor(S): ").upper()

class game:

    def __init__(self, a, b):
        self.a = a
        self.b = b

    def gameRule(self):

        if self.a == 'R':
            if self.b == 'P':
                print("Player 2 Win")
            elif self.b == 'S':
                print("Player 2 Lose")
            elif self.a == self.b:
                print("Tie")
            else:
                print("Please! Choose correct option")
        if self.a == 'S':
            if self.b == 'R':
                print("Player 2 Win")
            elif self.b == 'P':
                print("Player 2 Lose")
            elif self.a == self.b:
                print("Tie")
            else:
                print("Please! Choose correct option")
        if self.a == 'P':
            if self.b == 'R':
                print("Player 2 Lose")
            elif self.b == 'S':
                print("Player 2 Win")
            elif self.a == self.b:
                print("Tie")
            else:
                print("Please! Choose correct option")



RPS_game = game(player1, player2)
RPS_game.gameRule()
print("player 1 chose", str(player1))
