# Einführung: Iterieren von Mustern mit Listen

# Aufgabe 1 :
# Säcke voller Gold
#Wie viel wiegen sie insgesamt?
sacks = [2.33, 4.1, 8.5, 6.66, 2.4]
total_weight = 0
for sack in sacks:
    total_weight += sack
print("Gesamtgewicht:", total_weight)

# Die Flucht
# Nur Säcke ≤ 5 kg behalten. Wie viel wiegen die verbleibenden?
sacks = [2.33, 4.1, 8.5, 6.66, 2.4]
remaining_weight = 0
for sack in sacks:
    if sack <= 5:
        remaining_weight += sack
print("Verbleibendes Gewicht:", remaining_weight)

# Pechsträhne
# Wie viele Ketten haben genau 13 Perlen?
necklaces = [12, 13, 22, 18, 13, 10, 30, 15, 13, 12]
count_13 = 0
for n in necklaces:
    if n == 13:
        count_13 += 1
print("Anzahl Ketten mit 13 Perlen:", count_13)

# Häufige Namen
# Wie viele davon beginnen mit „H“?
# Wie viele davon beginnen mit „L“ und haben 4 Buchstaben?
names = ["Emma", "Felix", "Henry", "Linn", "Lina", "Felix", "Hannah", "Noah", "Marie", "Leon"]

# Namen, die mit H beginnen
count_H = 0
for name in names:
    if name.startswith("H"):
        count_H += 1

# Namen, die mit L beginnen und 4 Buchstaben haben
count_L4 = 0
for name in names:
    if name.startswith("L") and len(name) == 4:
        count_L4 += 1

print("Beginnen mit H:", count_H)
print("Beginnen mit L und haben 4 Buchstaben:", count_L4)

# Wie viele davon beginnen mit „H“?
# Wie viele davon beginnen mit „L“ und haben 4 Buchstaben?
def get_name_stats(names_list):
    count_names_starting_with_h = 0
    count_names_starting_with_l_and_4_chars_long = 0
    for name in names_list:
        if name.startswith("H"):
            count_names_starting_with_h +=1
        elif name.startswith("L") and len(name) == 4:
            count_names_starting_with_l_and_4_chars_long += 1
    return count_names_starting_with_h, count_names_starting_with_l_and_4_chars_long

count_names_starting_with_h, count_names_starting_with_l_and_4_chars_long = get_name_stats(names)
print(f"# Names starting with H: {count_names_starting_with_h}")
print(f"# Names starting with L and 4 chars long: {count_names_starting_with_l_and_4_chars_long}")

# Aufgabe 2 : Lagerhaus
# Im Lager habe ich 8 große Kisten, jede enthält 4 mittelgroße Kisten, die jeweils 6 kleine Kisten enthalten.
# Wie viele Kisten habe ich insgesamt?
boxes = [8, 4, 6]

large = boxes[0]
medium = large * boxes[1]
small = medium * boxes[2]

total = large + medium + small

print("Gesamtanzahl Kisten:", total)

# Bonus: Klassendurchschnitt
# Ich habe endlich alle Tests meiner Studenten bewertet.
# Wie ist der Durchschnitt der Klasse?
grades = [1.0, 2.1, 1.5, 3.0, 1.0, 1.2, 3.5, 1.0]

total = 0
for grade in grades:
    total += grade

average = total / len(grades)

print("Klassendurchschnitt:", average)

# Bonus: 5km-Lauf
# Ich gehe jeden Tag 5 km laufen und zeichne meine Zeiten auf.
# War mein schnellster Lauf?
times = [31.3, 29.8, 29.4, 30.3, 28.9, 29.4]

fastest = times[0]
for time in times:
    if time < fastest:
        fastest = time

print("Schnellster Lauf:", fastest, "Minuten")


