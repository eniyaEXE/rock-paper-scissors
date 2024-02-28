# ROCK PAPER SCISSORS
import random
import time

def clear():
    for _ in range(0, 10):
        print("\n")

clear()
print("welcome!")
time.sleep(1)

loopRunning = 1
errorCount = 0
wins = 0
losses = 0
draws = 0

while loopRunning == 1:
    pcMove = random.randint(1,3)                # randomly selects rock, paper, or scissors
    playerMove = input("\nplease type rock, paper, or scissors (Q to quit): ")        # asks player for move
    moveDict = {"rock": 3, "scissors": 2, "paper": 1}
    pcMoveDict = {3: "rock", 2: "scissors", 1: "paper", -3: "rock"}

    if playerMove == "Q":
        clear()
        loopRunning = 0
        continue

    if pcMove == 1 and moveDict.get(playerMove) == 3: # small workaround for paper beats rock
        time.sleep(0.6)
        print("\nthe computer chose paper...")
        time.sleep(0.3)
        print("\nyou lose...")
        print("wins: {0}    draws: {1}    losses: {2}".format(wins, draws, losses))
        time.sleep(2)
        continue

    if moveDict.get(playerMove) == 1 and pcMove == 3: # correction for paper beats rock
        pcMove = -3

    if moveDict.get(playerMove, 0) == 0:
        if errorCount == 2:
            print("\ncome on...")
            time.sleep(1)
            errorCount = 0
            continue
        print("\nplease enter a valid answer")
        errorCount += 1
        continue

    time.sleep(0.6)

    print("\nthe computer chose {0}...".format(pcMoveDict.get(pcMove)))

    time.sleep(0.3)

    # determines outcome of game:
    if moveDict.get(playerMove) == pcMove:
        print("\nit's a draw!")
        draws += 1

    elif moveDict.get(playerMove) > pcMove:
        print("\nyou win!")
        wins += 1

    else:
        print("\nyou lose...")
        losses += 1

    print("wins: {0}    draws: {1}    losses: {2}".format(wins, draws, losses))
    time.sleep(2)