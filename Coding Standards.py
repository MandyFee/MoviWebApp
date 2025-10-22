# Aufgabe 1
# Originalcode
def categorizeAge(AGE):
    if AGE<13:
        return "Child"
    else:
        if AGE<20:
            return "Teen"
        else:
            if AGE<60:
                return "Adult"
            else:
                return "Senior"
# Verbesserte Version
def categorize_age(age):
    """
    Bestimmt die Alterskategorie einer Person.

    Parameter:
        age (int): Das Alter der Person in Jahren.

    Rückgabe:
        str: Eine der Kategorien "Child", "Teen", "Adult" oder "Senior".
    """
    if age < 13:
        return "Child"
    elif age < 20:
        return "Teen"
    elif age < 60:
        return "Adult"
    else:
        return "Senior"

# Aufgabe 2
# Originalcode
def Func1(Data):
 tmp = []
 for x in Data:
   if x%2==0:
   tmp.append(x)
 return tmp
# Verbesserte Version
def get_even_numbers(data):
    """
    Gibt alle geraden Zahlen aus einer Liste zurück.

    Parameter:
        data (list[int]): Liste von ganzen Zahlen.

    Rückgabe:
        list[int]: Neue Liste mit nur den geraden Zahlen.
    """
    tmp = []
    for x in data:
        if x % 2 == 0:
            tmp.append(x)
    return tmp

# Aufgabe 3
# Originalcode
def processdata(data):
    # Create empty list
    result = [   ]
    # Loop through data
    for item in data:
        # Multiply by 2
        x = item * 2
        # Append to list
        result.append(x)
    # Return result
    return result
# Verbesserte Version
def double_values(data):
    """
    Verdoppelt jede Zahl in einer Liste.

    Parameter:
        data (list[int | float]): Liste von Zahlen.

    Rückgabe:
        list[int | float]: Liste mit verdoppelten Werten.
    """
    result = []
    for item in data:
        result.append(item * 2)
    return result

# Aufgabe 4
# Originalcode
def fnd_mx(lst):
    max_val = lst[0]
    for i in range(1, len(lst)):
      if lst[i] > max_val:
        max_val = lst[i]
    return max_val
# Verbesserte Version
def find_max_value(numbers):
    """
    Gibt den größten Wert in einer Liste zurück.

    Parameter:
        numbers (list[int | float]): Liste von Zahlen.

    Rückgabe:
        int | float: Der größte Wert in der Liste.

    Fehler:
        ValueError: Wenn die Liste leer ist.
    """
    if not numbers:
        raise ValueError("Die Liste darf nicht leer sein.")

    max_val = numbers[0]
    for i in range(1, len(numbers)):
        if numbers[i] > max_val:
            max_val = numbers[i]
    return max_val

# Aufgabe 5
# Originalcode
def print_now_and_get_minutes_in_year(years):
		print(now.time())
    return years * 60 * 24 * 365
# Verbesserte Version
from datetime import datetime

def print_now_and_get_minutes_in_year(years):
    """
    Gibt die aktuelle Uhrzeit aus und berechnet die Minutenanzahl
    für eine bestimmte Jahreszahl (ohne Schaltjahre).
    """
    now = datetime.now()
    print(now.time())
    return years * 60 * 24 * 365

# Aufgabe 6
# Originalcode
def lol(numbers):
    out = []
    for l in numbers:
        if l>= 2:
            #good flag
            notgood = False
            #chaeck if prime
            for i in range(2,l):
                if l % i == 0:
                    notgood=True; break
            if not notgood:
                out.append(l)
    return out
# Verbesserte Version
def is_prime(num):
    """
    Prüft, ob eine Zahl eine Primzahl ist.

    Parameter:
        num (int): Die zu prüfende Zahl.

    Rückgabe:
        bool: True, wenn Primzahl, sonst False.
    """
    if num < 2:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True


def filter_primes(numbers):
    """
    Gibt eine Liste aller Primzahlen aus einer gegebenen Zahlenliste zurück.
    """
    return [num for num in numbers if is_prime(num)]

# Aufgabe 7
# Originalcode
def A(p, n=10):
    """
    Analyze word frequency in a text file.
    Args:
        p (str): Path to the text file
        n (int): Number of top frequent words to return

    Returns:
        list: Top N most frequent words with their counts
    """
    z = {}
    try:
        f = open(p, 'r')
        t = f.read().lower()
        f.close()
        w = t.split()
        for x in w:
            x = x.strip('.,!?():;[]"\'')
            if x != '':
                if x in z:
                    z[x] += 1
                else:
                    z[x] = 1

        y = list(z.items())
        for m in range(len(y)):
            for k in range(0, len(y) - m - 1):
                if y[k][1] < y[k + 1][1]:
                    y[k], y[k + 1] = y[k + 1], y[k]
        return y[:n]
    except:
        return "err"
# Verbesserte Version
def analyze_word_frequency(file_path, n=10):
    """
    Analysiert die Wortfrequenz in einer Textdatei.

    Parameter:
        file_path (str): Pfad zur Textdatei.
        n (int): Anzahl der häufigsten Wörter, die zurückgegeben werden.

    Rückgabe:
        list[tuple]: Liste der Top-n-Wörter und deren Häufigkeit.
    """
    word_count = {}

    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            text = file.read().lower()

        words = text.split()
        for word in words:
            cleaned_word = word.strip('.,!?():;[]"\'')
            if cleaned_word:
                word_count[cleaned_word] = word_count.get(cleaned_word, 0) + 1

        sorted_words = sorted(word_count.items(), key=lambda item: item[1], reverse=True)
        return sorted_words[:n]

    except FileNotFoundError:
        return f"Datei nicht gefunden: {file_path}"
    except Exception as e:
        return f"Fehler: {e}"
