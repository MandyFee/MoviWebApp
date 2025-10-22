# Aufgabe 1
# Schritt 1: Dictionary mit Filmen und Preisen erstellen
movies_prices = dict ({
    "Inception": 12,
    "Avatar": 15,
    "Moana": 8
})

# Schritt 2: Einen neuen Film hinzufügen (zum Beispiel "Frozen" mit Preis 9)
movies_prices["Frozen"] = 9

# Schritt 3: Preis von "Inception" ändern auf 10
movies_prices["Inception"] = 10

# Schritt 4: Nur die Filmtitel ausgeben
print("Filmtitel:")
for title in movies_prices:
    print(title)

# Schritt 5: Menü lesbar anzeigen mit f-strings
print("\nKino-Menü:")
for title, price in movies_prices.items():
    print(f"{title} - ${price}")

# Aufgabe 2
# Unser Dictionary mit den Filmen und Preisen
movies_prices = {
    "Inception": 10,
    "Avatar": 15,
    "Moana": 8,
    "Frozen": 9
}

# Funktion zum Hinzufügen eines neuen Films
def add_movie(title, price):
    if title in movies_prices:
        print(f"🎥 Der Film '{title}' ist bereits im System.")
    else:
        movies_prices[title] = price
        print(f"✅ Der Film '{title}' wurde mit dem Preis ${price} hinzugefügt.")

# Funktion zum Aktualisieren eines bestehenden Preises
def update_price(title, new_price):
    if title in movies_prices:
        movies_prices[title] = new_price
        print(f"🔁 Der Preis von '{title}' wurde auf ${new_price} aktualisiert.")
    else:
        print(f"❌ Film '{title}' wurde nicht gefunden.")

# Funktion zum Abrufen des Ticketpreises
def get_ticket_price(title):
    if title in movies_prices:
        return movies_prices[title]
    else:
        return "Movie not found!"

# Funktion zum Entfernen eines Films
def remove_movie(title):
    if title in movies_prices:
        del movies_prices[title]
        print(f"🗑️ Der Film '{title}' wurde entfernt.")
    else:
        print(f"⚠️ Der Film '{title}' ist nicht im System.")

# ----- Testaufrufe -----
print("\n--- TEST ---")
add_movie("The Matrix", 10)
add_movie("Avatar", 20)              # sollte anzeigen, dass Avatar schon da ist
update_price("Moana", 12)
update_price("Titanic", 11)          # nicht vorhanden
print(f"🎟️ Preis für 'Inception': ${get_ticket_price('Inception')}")
print(f"🎟️ Preis für 'Titanic': {get_ticket_price('Titanic')}")
remove_movie("Frozen")
remove_movie("Shrek")                # nicht vorhanden

# Aktuelle Filmliste anzeigen
print("\n📋 Aktuelles Kino-Menü:")
for title, price in movies_prices.items():
    print(f"{title} - ${price}")

# Aufgabe 3
# Vorgegebenes Dictionary mit Schülernamen und deren Notenlisten
student_grades = {
    "emma_schneider": [88, 92, 79],
    "jonas_muller": [76, 81, 85],
    "ben_fischer": [90, 87, 93],
    "felix_wagner": [72, 75, 70],
    "lena_hoffmann": [95, 89, 91]
}
print("🎯 Beste Note pro Schüler:")
for name, grades in student_grades.items():
    best_grade = max(grades)
    print(f"{name}: {best_grade}")
import math  # Für Abrunden

print("\n📘 Durchschnittsnote pro Schüler (abgerundet):")
for name, grades in student_grades.items():
    average = sum(grades) / len(grades)
    rounded_average = math.floor(average)
    print(f"{name}: {rounded_average}")
def find_top_student(student_grades):
    best_student = ""
    highest_average = 0

    for name, grades in student_grades.items():
        average = sum(grades) / len(grades)
        if average > highest_average:
            highest_average = average
            best_student = name

    return best_student
top_student = find_top_student(student_grades)
print(f"\n🏆 Schüler mit der besten Durchschnittsnote: {top_student}")
