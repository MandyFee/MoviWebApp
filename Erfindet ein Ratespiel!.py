#Create a “Guessing Game”!
#For each game, select a random number from 1 to 9 (inclusive). The player has three attempts to guess the number. Inform the player if they win or lose.
#Extra
#After each guess, “throw a dice” by selecting a number from 1 to 6 (inclusive). If the “dice” shows 5 or 6, the player gets another attempt to guess the number. Inform the player of the dice results.

import random

# Zufallszahl zwischen 1 und 9 wählen
secret_number = random.randint(1, 9)
attempts = 3

print("Willkommen beim Zahlenratespiel!")
print("Ich habe eine Zahl zwischen 1 und 9 ausgewählt.")
print("Du hast 3 Versuche, sie zu erraten.")

while attempts > 0:
    # Spieler um Eingabe bitten
    guess = input("Bitte gib deine Zahl ein: ")

    # Prüfen, ob die Eingabe eine Zahl ist
    if not guess.isdigit():
        print("Bitte nur Zahlen eingeben.")
        continue

    guess = int(guess)

    if guess == secret_number:
        print("Herzlichen Glückwunsch! Du hast die Zahl erraten!")
        break
    else:
        attempts -= 1
        print("Leider falsch.")

        # Extra: Würfeln, um evtl. einen Bonusversuch zu bekommen
        dice = random.randint(1, 6)
        print(f"Du wirfst einen Würfel... Er zeigt: {dice}")
        if dice == 5 or dice == 6:
            attempts += 1
            print("Glück gehabt! Du bekommst einen zusätzlichen Versuch.")

        if attempts > 0:
            print(f"Du hast noch {attempts} Versuche übrig.")
        else:
            print(f"Keine Versuche mehr. Die richtige Zahl war {secret_number}.")
