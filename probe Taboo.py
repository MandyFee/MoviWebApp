import wikipedia as wiki
import random

def begruessung():
    name = input("Wie heißt du? ")
    print(f"Hallo {name}, willkommen zu Taboo!")

def runden_abfrage():
    while True:
        try:
            runden = int(input("Wie viele Runden möchtest du spielen? (1-9) "))
            if 1 <= runden <= 9:
                return runden
            else:
                print("Bitte eine Zahl zwischen 1 und 9 eingeben.")
        except ValueError:
            print("Bitte eine gültige Zahl eingeben.")

def daten_holen(anzahl_runden):
    artikel_liste = []
    content_dict = {}
    while len(artikel_liste) < anzahl_runden:
        try:
            artikel = wiki.random()
            if artikel in artikel_liste:
                continue  # keine Duplikate
            seite = wiki.WikipediaPage(artikel)
            content_dict[artikel] = {
                "inhalt": seite.content,
                "links": seite.links
            }
            artikel_liste.append(artikel)
        except (wiki.DisambiguationError, wiki.PageError, wiki.HTTPTimeoutError):
            continue  # Artikel überspringen, wenn es ein Fehler gibt
    return content_dict, artikel_liste

def snippits_erstellen(content_dict, artikel_liste):
    snippits_dict = {}
    for artikel in artikel_liste:
        inhalt = content_dict[artikel]["inhalt"]
        stichworte = content_dict[artikel]["links"]
        passagen = inhalt.split("\n")
        saetze = []
        for passage in passagen:
            for satz in passage.split("."):
                satz = satz.strip()
                if satz:
                    saetze.append(satz)
        gefundene_snippits = []
        for satz in saetze:
            for stichwort in stichworte:
                if stichwort in satz:
                    gefundene_snippits.append(satz)
                    break
        # Falls keine Snippets gefunden, einfach 3 zufällige Sätze nehmen
        if not gefundene_snippits:
            gefundene_snippits = random.sample(saetze, min(3, len(saetze)))
        snippits_dict[artikel] = gefundene_snippits
    return snippits_dict

def frage_stellen(snippits_dict, artikel_liste, content_dict):
    punkte = 0
    for artikel in artikel_liste:
        if not snippits_dict[artikel]:
            print(f"Keine passenden Snippets für '{artikel}', Runde übersprungen.")
            continue
        snippit = random.choice(snippits_dict[artikel])
        print("\nHier ist dein Snippet:")
        print(snippit)

        rate_versuche = 3
        richtig = False
        while rate_versuche > 0 and not richtig:
            antwort = input("Welcher Artikel wird hier beschrieben? ")
            if antwort.lower() == artikel.lower():
                print("Richtig! 🎉")
                punkte += 1
                richtig = True
            else:
                rate_versuche -= 1
                print(f"Falsch. Versuche übrig: {rate_versuche}")

                if rate_versuche == 2:
                    erster_absatz = content_dict[artikel]["inhalt"].split("\n")[0]
                    print("\n💡 Hinweis 1 (erster Absatz ohne den gesuchten Begriff):")
                    print(erster_absatz.replace(artikel, "_____"))
                elif rate_versuche == 1:
                    print("\n💡 Hinweis 2 (gesamter Artikeltext ohne den gesuchten Begriff):")
                    print(content_dict[artikel]["inhalt"].replace(artikel, "_____"))
                elif rate_versuche == 0:
                    print(f"\n💡 Hinweis 3 (Anfangsbuchstabe): {artikel[0]}")
        if not richtig:
            print(f"Die richtige Antwort wäre: {artikel}")

    print(f"\nSpiel vorbei! Du hast {punkte} von {len(artikel_liste)} Punkten erreicht.")

def main():
    begruessung()
    runden = runden_abfrage()
    content_dict, artikel_liste = daten_holen(runden)
    snippits_dict = snippits_erstellen(content_dict, artikel_liste)
    frage_stellen(snippits_dict, artikel_liste, content_dict)

if __name__ == "__main__":
    main()
