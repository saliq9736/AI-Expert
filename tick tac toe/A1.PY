from colorama import init,Fore
import random
init(autoreset=True)

def show(board):
    for i in range(0,9,3):
        print(
            Fore.RED + board[i],"|",
            Fore.BLUE + board[i+1],"|",
            Fore.RED + board[i+2]
        )
        if i < 6:
            print("---+---+---")


def win (board,player):
    ways = [
        (0,1,2),(3,4,5),(6,7,8), 
        (0,3,6),(1,4,7),(2,5,8), 
        (0,4,8),(2,4,6)    
    ]
    for a,b,c in ways: 
        if board[a] == board[b] == board[c] == player:
            return True
    return False
def game():
        board = list ("123456789")
        print(Fore.GREEN + "Welcome to Tic Tac Toe!")
        while True:
            show (board)
            move = int(input("choose a position from(1-9): ")) - 1
            if board[move].isdigit():
                board [move] = "X"
            else:
                print(Fore.YELLOW +"position already taken")
                continue
            if win (board,"X"):
                show(board)
                print(Fore.GREEN + "You win!")
                break
            empty= [i for i in range (9 )if board [i].isdigit()]
            if not empty:
                print(Fore.YELLOW + "It's a tie!")
                break
            ai_move = random.choice(empty)
            board[ai_move] = "O"
            if win (board,"O"):
                show(board)
                print(Fore.RED + "AI wins!")
                break
game()
