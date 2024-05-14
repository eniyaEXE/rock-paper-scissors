# ROCK PAPER SCISSORS
import random

errorCount = 0
wins = 0
losses = 0
draws = 0
gamesPlayed = 0

red = "\033[31m"        # ANSI color codes borrowed from graphing-calculator
green = "\033[32m"
blue = "\033[34m"
yellow = "\033[33m"
clear = "\033[0m"

moveDict = {"rock": 3, 
            "scissors": 2, 
            "paper": 1,
            "correction": -3
            }
    
pcMoveDict = {3: "rock", 
              2: "scissors", 
              1: "paper", 
              -3: "rock"
              }

print("welcome!")

while True:
    pcMove = random.randint(1,3)                # randomly selects rock, paper, or scissors
    playerMove = input(f"\n{blue}please enter your move{clear}: ").lower()        # asks player for move
    
    if moveDict.get(playerMove) == None:
        if errorCount == 2:
            print(f"\n{red}come on...{clear}")
            errorCount = 0
            continue

        print(f"\n{red}please enter a valid answer{clear}")
        errorCount += 1
        continue

    gamesPlayed += 1

    if pcMove == 1 and moveDict[playerMove] == 3: # small workaround for paper beats rock
        playerMove = "correction"

    elif moveDict[playerMove] == 1 and pcMove == 3: # correction for paper beats rock
        pcMove = -3

    print(f"\nthe computer chose {blue}{pcMoveDict[pcMove]}{clear}...")

    # determines outcome of game:
    if moveDict[playerMove] == pcMove:
        print(f"\n{yellow}it's a draw!")
        draws += 1

    elif moveDict[playerMove] > pcMove:
        print(f"\n{green}you win!")
        wins += 1

    else:
        print(f"\n{red}you lose...")
        losses += 1

    winPercentage = round((wins / gamesPlayed) * 100, 2)

    print(f"{green}wins{clear}: {wins}    {yellow}draws{clear}: {draws}    {red}losses{clear}: {losses}")
    print(f"{green}percentage won{clear}: {winPercentage}%\n--------------------------------------------")