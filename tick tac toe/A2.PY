
import random
from colorama import init, Fore

init(autoreset=True)

choices = ["rock", "paper", "scissors"]

player = input(Fore.YELLOW + "Choose rock, paper or scissors: ").lower()
computer = random.choice(choices)

print(Fore.BLUE + "Computer chose:", computer)

if player == computer:
    print(Fore.YELLOW + "It's a tie!")

elif (player == "rock" and computer == "scissors") or \
     (player == "paper" and computer == "rock") or \
     (player == "scissors" and computer == "paper"):
    print(Fore.GREEN + "You win!")

else:
    print(Fore.RED + "Computer wins!")