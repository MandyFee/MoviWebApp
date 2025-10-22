# Aufgabe 1
# Wir starten mit einer leeren Variable
number = None

# Solange die Zahl NICHT gerade ist, soll die Schleife weiterlaufen
while True:
    # Benutzer eingabe
    number = int(input("Bitte gib eine Zahl ein: "))

    # Prüfen, ob die Zahl gerade ist (durch 2 teilbar)
    if number % 2 == 0:
        print("Das ist eine gerade Zahl. Programm wird beendet.")
        break  # Schleife stoppen
    else:
        print("Das war eine ungerade Zahl. Versuch's nochmal!")

# Aufgabe 2
# Wir zählen, wie viele ungerade Zahlen eingegeben wurden
odd_count = 0

# Solange wir weniger als 4 ungerade Zahlen haben, wiederholen wir
while odd_count < 4:
    number = int(input("Gib eine Zahl ein: "))

    # Prüfen, ob die Zahl ungerade ist
    if number % 2 != 0:
        odd_count += 1  # Zähler für ungerade Zahlen erhöhen
        print(f"Das war ungerade Nummer {odd_count}!")
    else:
        print("Das war eine gerade Zahl. Die zählt nicht!")

print("Du hast 4 ungerade Zahlen eingegeben. Ende ✨")

# Aufgabe 3
# Liste der gültigen Menü-Optionen
menu = ["fish", "chips", "bread"]

# Wiederhole, bis eine gültige Bestellung eingegeben wurde
while True:
    order = input("Was möchtest du bestellen? (fish, chips, bread): ").lower()

    # Prüfen, ob die Eingabe im Menü ist
    if order in menu:
        print("Order successfully placed ✅")
        break  # Schleife beenden
    else:
        print("Dieses Gericht ist nicht auf der Karte. Versuch's nochmal 🍽️")

# Bonus
# Wiederhole solange, bis eine gültige E-Mail eingegeben wird
while True:
    email = input("Gib deine E-Mail-Adresse ein: ")

    # Prüfen, ob ein @ enthalten ist
    if "@" in email:
        # In zwei Teile aufteilen: vor dem @ (prefix), nach dem @ (domain)
        parts = email.split("@")

        if len(parts) == 2:  # Es muss genau ein @ geben
            prefix = parts[0]
            domain = parts[1]

            # Bedingungen prüfen
            if len(prefix) >= 5 and (domain == "mail.com" or domain == "mail.net"):
                print("✅ E-Mail-Adresse ist gültig. Willkommen, " + prefix + "!")
                break
            else:
                print(
                    "❌ Ungültig! Stelle sicher, dass der Name mindestens 5 Zeichen hat und die Domain mail.com oder mail.net ist.")
        else:
            print("❌ Ungültiges Format! Bitte gib nur eine @-Adresse ein.")
    else:
        print("❌ Keine @-Adresse erkannt. Versuch's nochmal.")
