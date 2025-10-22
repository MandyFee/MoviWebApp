# 📋 Student Information
student_info = [
    {"name": "Alice", "age": 18, "gender": "female"},
    {"name": "Bob", "age": 17, "gender": "male"},
    {"name": "Charlie", "age": 18, "gender": "male"}
]

# 📊 Student Grades
student_grades = [
    [85, 90, 88],
    [75, 80, 82],
    [92, 95, 89]
]

# 📝 Student Details
student_details = {
    "Alice": {"city": "New York", "grade_level": "Senior"},
    "Bob": {"city": "Los Angeles", "grade_level": "Junior"},
    "Charlie": {"city": "Chicago", "grade_level": "Senior"}
}

# --------------------------------------------------------
# 🔹 Schritt 1: Durchschnitt berechnen
# 🔹 Schritt 2: Daten aus allen Strukturen zusammenführen
# 🔹 Schritt 3: Ausgabe mit Name, Alter, Klassenstufe & Durchschnitt
# 🔹 Bonus: Schüler mit höchstem Schnitt + Stadt
# --------------------------------------------------------

averages = []  # Speichert (Name, Durchschnitt) für Bonus-Aufgabe

for i, info in enumerate(student_info):
    name = info["name"]
    age = info["age"]
    grades = student_grades[i]
    avg = sum(grades) / len(grades)

    # Speichere für Bonus
    averages.append((name, avg))

    grade_level = student_details[name]["grade_level"]

    print(f"Name: {name}, Alter: {age}, Klassenstufe: {grade_level}, Durchschnitt: {avg:.2f}")

# ✨ Bonus: Schüler mit bestem Schnitt finden
best_student = max(averages, key=lambda x: x[1])[0]  # Name des besten
best_city = student_details[best_student]["city"]

print("\n✨ Bonus Aufgabe:")
print(f"Der Schüler mit dem höchsten Notendurchschnitt ist {best_student} aus {best_city}.")
