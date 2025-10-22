import random
import wikipedia
import warnings

# Warnungen ausschalten
warnings.filterwarnings("ignore", category=UserWarning, module="wikipedia")
wikipedia.set_lang("de")

# Begrüßung
name = input("Hey! Wie heißt du? ")
print(f"Willkommen {name}! Lass uns Memory spielen! 🎉")

# 5 zufällige Wikipedia-Themen für 10 Karten (5 Paare)
karten = []
while len(karten) < 10:
    try:
        thema = wikipedia.random()
        satz = wikipedia.summary(thema, sentences=1)
        if (thema, satz) not in karten:
            karten += [(thema, satz)] * 2  # Paar erstellen
    except:
        continue

random.shuffle(karten)  # Karten mischen

# Punkte und Runden
punkte = 0
runden = int(input("Wie viele Runden möchtest du spielen? (1-9) "))

# Spiel starten
for r in range(1, runden+1):
    print(f"\n--- Runde {r} ---")
    versuche = 3
    sichtbar = ["X"] * len(karten)

    while versuche > 0:
        print(" ".join([f"{i}:{sichtbar[i]}" for i in range(len(sichtbar))]))
        try:
            w1, w2 = int(input("Erste Karte (0-9): ")), int(input("Zweite Karte (0-9): "))
        except:
            print("Bitte Zahlen eingeben!")
            continue
        if w1 == w2 or not (0 <= w1 < 10) or not (0 <= w2 < 10):
            print("Ungültige Auswahl! Wähle zwei verschiedene Karten von 0 bis 9.")
            continue

        sichtbar[w1], sichtbar[w2] = karten[w1][0], karten[w2][0]
        print(" ".join([f"{i}:{sichtbar[i]}" for i in range(len(sichtbar))]))

        if karten[w1][0] == karten[w2][0]:
            print("Treffer! 🎉")
            punkte += 1
        else:
            print("Leider falsch 😅")
            sichtbar[w1], sichtbar[w2] = "X", "X"

        versuche -= 1
        print(f"Noch {versuche} Versuche übrig")

print(f"\nSpiel vorbei! {name}, du hast {punkte} Punkte gesammelt! 🏆")
