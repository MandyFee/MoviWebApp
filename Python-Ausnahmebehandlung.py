# Aufgabe 1
#1.Ausführung des Codes & Ausnahme
def is_divisible_by(number, divisor):
    return number % divisor == 0

print(is_divisible_by(10, 2))
print(is_divisible_by(10, "2"))  # Causes an exception
#✅ Erste Ausgabe:
#is_divisible_by(10, 2) → True

#❌ Zweite Ausgabe:
#is_divisible_by(10, "2") → führt zu einer Ausnahme:
#Fehler:TypeError: not all arguments converted during string formatting
#Typ: TypeError (weil man nicht % mit einer Zahl und einem String kombinieren kann).

#2. Lösung mit if/else (einfache Bedingungen)
def is_divisible_by(number, divisor):
    if isinstance(divisor, int) and isinstance(number, int):
        return number % divisor == 0
    else:
        return False  # oder eine Meldung wie "Ungültiger Divisor"

print(is_divisible_by(10, 2))     # ✅ True
print(is_divisible_by(10, "2"))   # ✅ False (stürzt nicht mehr ab)

#3. Lösung mit try/except/finally
def is_divisible_by(number, divisor):
    try:
        return number % divisor == 0
    except TypeError:
        print("❌ Ungültiger Datentyp für divisor!")
        return False
    finally:
        print(f"Überprüfung abgeschlossen: number={number}, divisor={divisor}")

print(is_divisible_by(10, 2))     # ✅ True
print(is_divisible_by(10, "2"))   # ❌ Meldung + False

# Aufgabe 2
#1. Code ausführen
def add_percentage(price, percentage):
    return price + (percentage * price)

print(add_percentage(100, 0.1))
print(add_percentage(100, "0.05"))  # Causes an exception
#✅ Erste Ausgabe:
#add_percentage(100, 0.1) → 110.0

#❌ Zweite Ausgabe:
#add_percentage(100, "0.05") → führt zu einer Ausnahme:
#Fehler:TypeError: can't multiply sequence by non-int of type 'float'
#Typ: TypeError (weil man eine Zahl nicht mit einem String multiplizieren kann, außer wenn es ein ganzzahliger Multiplikator ist, z. B. "abc" * 3).

#2. Lösung mit if/else
def add_percentage(price, percentage):
    if isinstance(price, (int, float)) and isinstance(percentage, (int, float)):
        return price + (percentage * price)
    else:
        print("❌ Ungültige Eingabe – bitte Zahlen verwenden.")
        return None

print(add_percentage(100, 0.1))     # ✅ 110.0
print(add_percentage(100, "0.05"))  # ❌ Fehlermeldung, kein Absturz

#3. Lösung mit try/except/finally
def add_percentage(price, percentage):
    try:
        return price + (percentage * price)
    except TypeError:
        print("❌ Typfehler: Bitte Zahlen angeben (int oder float).")
        return None
    finally:
        print(f"Überprüfung abgeschlossen: price={price}, percentage={percentage}")

print(add_percentage(100, 0.1))     # ✅ 110.0
print(add_percentage(100, "0.05"))  # ❌ Meldung, kein Absturz

# Aufgabe 3
#1. Problem im Originalcode
def get_grade(database, student_name):
    return database[student_name]

db = {"John": "A+", "Mary": "B", "Jane": "C", "Thomas": "B+"}

name = "John"
print(get_grade(db, name))   # ✅ funktioniert

name = "Johnn"
print(get_grade(db, name))   # ❌ KeyError
#❌ Hier entsteht ein KeyError, weil "Johnn" nicht im Dictionary (db) existiert.

#2. Lösung mit Ausnahmebehandlung (try/except)
def get_grade(database, student_name):
    try:
        return database[student_name]
    except KeyError:
        print(f"❌ Schüler '{student_name}' nicht gefunden! Bitte Eingabe überprüfen.")
        return None

db = {"John": "A+", "Mary": "B", "Jane": "C", "Thomas": "B+"}

print(get_grade(db, "John"))    # ✅ A+
print(get_grade(db, "Johnn"))   # ❌ Fehlermeldung

#3. Erweiterung: Suche unabhängig von Groß/Kleinschreibung
def get_grade(database, student_name):
    # Normalisiere Keys in Kleinbuchstaben
    normalized_db = {name.lower(): grade for name, grade in database.items()}

    try:
        return normalized_db[student_name.lower()]
    except KeyError:
        print(f"❌ Schüler '{student_name}' nicht gefunden! Bitte Eingabe überprüfen.")
        return None

db = {"John": "A+", "Mary": "B", "Jane": "C", "Thomas": "B+"}

print(get_grade(db, "John"))    # ✅ A+
print(get_grade(db, "john"))    # ✅ A+
print(get_grade(db, "JOHN"))    # ✅ A+
print(get_grade(db, "Johnn"))   # ❌ Meldung

# Bonus Aufgabe
#1. Angeforderte Fälle
#Die Funktion calculate_square(number) soll Fehler auslösen, wenn:
#❌ Der Benutzer eine Zeichenkette eingibt → TypeError
#❌ Die Zahl negativ ist → ValueError
#❌ Die Zahl kleiner als 1 oder größer als 100 ist → ValueError

#2. Lösungscode
def calculate_square(number):
    # Prüfen, ob Eingabe eine Zahl ist
    if not isinstance(number, (int, float)):
        raise TypeError("❌ Eingabe muss eine Zahl sein.")

    # Prüfen, ob Zahl negativ ist
    if number < 0:
        raise ValueError("❌ Negative Zahlen sind nicht erlaubt.")

    # Prüfen, ob Zahl im erlaubten Bereich liegt
    if number < 1 or number > 100:
        raise ValueError("❌ Zahl muss zwischen 1 und 100 liegen.")

    return number * number

# Aufruf mit Fehlerbehandlung
test_values = [10, -5, "abc", 0.5, 150]

for val in test_values:
    try:
        result = calculate_square(val)
        print(f"✅ Quadrat von {val} ist {result}")
    except TypeError as te:
        print(f"TypeError abgefangen: {te}")
    except ValueError as ve:
        print(f"ValueError abgefangen: {ve}")
