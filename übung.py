"""
def find_missing_number(nums):
    # Bereich bestimmen: von 1 bis max der Zahlen
    n = max(nums) if nums else 0
    expected = set(range(1, n + 1))  # alle Zahlen von 1 bis n
    actual = set(nums)               # Zahlen aus der Liste
    missing = expected - actual      # Differenz finden
    return missing.pop() if missing else None

# Beispiel
nums1 = [8, 4, 10, 2, 3, 5, 1, 9, 6]
print(find_missing_number(nums1))  # Output: 7
"""
"""
def sun_of_digits(text):
    total=0
    for char  in text:   # jeder Buchstaben/ Zahlen im String durchsuchen
        if char.isdigit():   # prüfen: ist es eine Ziffer?
            total += int(char)      # Ziffer in Zahl umwandeln und addieren
    return total

input_text = "abc123xyz45"
print(sun_of_digits(input_text))
"""
"""
def adjust_temperature(temps, hour):
    if 6<= hour <=9:
        delta = 2.0  #Morgens (6–9 Uhr): +2 °C auf jede Temperatur
    if 17<= hour <=20:
        delta = 3.0  #Abends (17–20 Uhr): –3 °C auf jede Temperatur
    if 0<= hour <=5:
        delta = 1.0  #Nachts (0–5 Uhr): –1 °C auf jede Temperatur
    else:
        delta = 0.0
    adjusted =[]
    for t in temps:
        new_value = t + delta
        adjusted.append(new_value)
    return adjusted
temps = [20.0, 22.5, 19.0]
print(adjust_temperature(temps, 7))
# Expected: [22.0, 24.5, 21.0] (morning boost)
print(adjust_temperature(temps, 18))
# Expected: [17.0, 19.5, 16.0] (evening cool down)
print(adjust_temperature(temps, 3))
# Expected: [19.0, 21.5, 18.0] (night time)
print(adjust_temperature(temps, 12))
# Expected: [20.0, 22.5, 19.0] (no change)
"""
"""
def filter_valid_students(students):
    valid=[]
    for s in students:
        if "name" not in s:
            continue
        name = s["name"]
        if name == "" or len(name) == 1:
            continue
        valid.append(s)
    return valid
# Test cases:
students = [
{"name": "Lizi", "age": 20},
{"name": "Rick", "age": 21},
{"age": 22},
{"name": "", "age": 23},
{"name": "Carlie", "age": 24},
{"name": "D", "age": 25},
{"name": "Eve", "age": 26}]
# Expected output:
# [{'name': 'Lizi', 'age': 20}, {'name': 'Rick', 'age': 21}, {'name': 'Carlie', 'age': 24}, {'name': 'Eve', 'age': 26}]
print(filter_valid_students(students))
"""