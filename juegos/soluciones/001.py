import random

choices = ["piedra", "papel", "tijera", "lagarto", "spock"]

def get_computer_choice():
    return random.choice(choices)

def get_winner(player_choice, computer_choice):
    if player_choice == computer_choice:
        return "empate"
    elif player_choice == "piedra" and (computer_choice == "tijera" or computer_choice == "lagarto"):
        return "jugador"
    elif player_choice == "papel" and (computer_choice == "piedra" or computer_choice == "spock"):
        return "jugador"
    elif player_choice == "tijera" and (computer_choice == "papel" or computer_choice == "lagarto"):
        return "jugador"
    elif player_choice == "lagarto" and (computer_choice == "papel" or computer_choice == "spock"):
        return "jugador"
    elif player_choice == "spock" and (computer_choice == "piedra" or computer_choice == "tijera"):
        return "jugador"
    else:
        return "computadora"
    
print("Piedra, Papel, Tijera, Lagarto, Spock")
player_choice = input("Ingresa tu elección (piedra, papel, tijera, lagarto, spock): ").lower()
if player_choice in choices:
    computer_choice = get_computer_choice()
    print(f"La computadora eligio: {computer_choice}")
    winner = get_winner(player_choice, computer_choice)
    match winner:
        case "jugador":
            print("Ganaste!")
        case "computadora":
            print("Perdiste!")
        case "empate":
            print("Empate!")
else:
    print("Elección inválida")

