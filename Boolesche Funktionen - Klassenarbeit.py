# Aufgabe 1
# Enthält die Zeichenfolge mindestens einen Punkt („.“)? Deutsch
# Does the string contain at least one dot (“.”)?
def contains_dot(s):
    for char in s:
        if char == ".":
            return True  # Early exit: Punkt gefunden
    return False
# Tests:
print(contains_dot("Hallo.Welt"))      # True
print(contains_dot("Keine Punkte"))    # False
print(contains_dot("..."))             # True

# Aufgabe 2
# Enthält die Zeichenfolge nur Dollar („$“)? Deutsch
# Does the string contain only dollars (“$”)?
def contains_only_dollars(s):
    if not s:
        return False  # Leerer String zählt nicht
    for char in s:
        if char != "$":
            return False  # Early exit: ein anderes Zeichen gefunden
    return True
# Tests:
print(contains_only_dollars("$$$$$"))      # True
print(contains_only_dollars("$money$"))    # False
print(contains_only_dollars(""))           # False

# Aufgabe 3
# Sind alle Zahlen in der Liste größer als 10 und kleiner als 20? Deutsch
# Is every number on a list lower than 20 but higher than 10?
def all_numbers_between_10_and_20(numbers):
    for number in numbers:
        if number <= 10 or number >= 20:
            return False  # Early exit: Zahl außerhalb des Bereichs
    return True
# Testen:
print(all_numbers_between_10_and_20([11, 15, 19]))   # True
print(all_numbers_between_10_and_20([10, 12, 18]))   # False
print(all_numbers_between_10_and_20([21, 12, 14]))   # False