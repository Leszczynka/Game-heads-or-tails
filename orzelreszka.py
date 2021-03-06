import random
from time import sleep

availableChoices = ["h", "t"]
playerPoints = 0
computerPoints = 0
print("Let's play a game heads or tails! The winner is the one who gains three points.")
while True:
    if playerPoints==3 and computerPoints==3:
        print("It's a draw.")
        break
    elif playerPoints==3:
        print("Congratulations, you won!")
        break
    elif computerPoints==3:
        print("The computer won the game.")
        break
    else:
        playerChoice = input("Enter h to choose heads or t to choice tails: ")

        while playerChoice not in availableChoices:
            playerChoice = input("Incorrect input, enter h or t: ")

        toss = random.choice(availableChoices)
        computerChoice = random.choice(availableChoices)

        for i in range(3, 0, -1):
            print(i)
            sleep(1)

        print("Computer choice is", computerChoice)
        print("Result of the coin toss", toss)

        if playerChoice == toss and computerChoice == toss:
            playerPoints += 1
            computerPoints += 1
            print("One point for the player and one point for the computer.")
        elif computerChoice == toss:
            computerPoints += 1
            print("One point for the computer.")
        elif playerChoice == toss:
            playerPoints += 1
            print("One point for the player")
        else:
            print("No one gained a point.")

print(f"Player's points: {playerPoints}\nComputer's points: {computerPoints}")
input()