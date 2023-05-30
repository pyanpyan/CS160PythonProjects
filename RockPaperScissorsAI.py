import random

options = ["rock", "paper", "scissors"]
#			0		1		 2
choices = options[:]

# Which option beats which
def thinker (ply, comp):
    #print("player", ply, options.index(ply))
    #print("computer", comp, options.index(comp))
    result = options.index(ply) - options.index(comp)
    result = result % 3
    #print(choices)
    if result == 1:
        choices.append(options[(options.index(ply) + 1) % 3])
        choices.remove(comp)
        print("You won!")
    elif result == 2:
        choices.append(comp)
        print("You lost!")
    elif result == 0:
        print("You tied!")
    return "" # 1 = player W, 2 = player L, 0 = T 


def shuffle (cards):
    for num in range(len(cards)):
        swap = random.randrange(len(cards))
        hold = cards[swap]
        cards[swap] = cards[num]
        cards[num] = hold
    
# Play instructions
print("Let's play Rock/Paper/Scissors!")
print("Rock smashes scissors, paper covers rock, and scissors cut paper.")

while True:
    # Randomly choose one
    #compchoice = random.choice(choices) --> previous randomization method
    shuffle(choices)
    compchoice = choices[0]
    
    # Get input
    plychoice = ""
    while plychoice not in options:
        plychoice = input("Rock, paper, or scissors?: ")
        plychoice = plychoice.lower()


    print("Computer picked:", compchoice)
    print("Player picked:", plychoice)
    print(thinker(plychoice, compchoice))