
import random
from colorama import Fore,init
init(autoreset=True)
places={
    "beaches":["Maldives","Bali","Hawaii","Phuket"],
    "mountains":["Swiss Alps","Rocky Mountains","Himalayas","Andes"],
    "cities":["New York","Tokyo","Paris","London","Barcelona"],
}
jokes=[
    "Why don't oysters donate to charity? Because they are shellfish!","What do you call a snowman in the summer? A puddle!",
    "Why did the mountain break up with the hill? It found someone more uplifting!","Why did the mountain go to therapy? It had too many peaks and valleys!",
    "Why did the city break up with the countryside? It needed more space!","Why did the city hire a detective? To find out who was stealing all the streetlights!"
]
print(Fore.CYAN+"="*40)
print(Fore.YELLOW+"Welcome to the Travelbot! Your personal travel assistant.")
print(Fore.CYAN+"="*40)
name=input(Fore.GREEN+"What's your name? ")
print(Fore.GREEN+f"\nHello,{name}! Let's plan your next adventure.")
print(Fore.GREEN+"type help to see commands.")
while True:
    msg=input(Fore.BLUE+f"{name}: ").lower().strip()
    if msg in ["exit","quit"]:
        print(Fore.RED+"Goodbye! Safe travels!")
        break
    elif "recommend" in msg:
        print(Fore.CYAN+"What type of destination are you interested in? (beaches/mountains/cities)")
        choice = input(Fore.BLUE+"Your choice: ").lower().strip()
        if choice in places:
            place=random.choice(places[choice])
            print(Fore.YELLOW+f"How about visiting {place}? It would be a great experience!")
        else:
            print(Fore.RED+"Sorry ivalid category")
    elif "pack" in msg:
        place=input(Fore.BLUE+"Where are you going? ")
        days=int(input(Fore.BLUE+"How many days will you be staying? "))
        print(Fore.GREEN+f"For a {days}-day trip to {place}, you should pack:")
        print("pack comfortable clothes")
        print("pack sunscreen and sunglasses")
        print("pack a camera to capture memories")
        print("pack a travel guide or map")
        print("bring chargers and powerbanks for your devices")
    elif "joke" in msg:
        joke=random.choice(jokes)
        print(Fore.YELLOW+joke)
    elif "help" in msg:
        print(Fore.CYAN+"Available commands:")
        print(Fore.GREEN+"recommend - Get a travel destination recommendation")
        print(Fore.GREEN+"pack - Get packing suggestions for your trip")
        print(Fore.GREEN+"joke - Hear a travel-related joke")
        print(Fore.GREEN+"exit/quit - Exit the Travelbot")
    else:
        print(Fore.RED+"Sorry, I didn't understand that command. Type 'help' to see available commands.")
