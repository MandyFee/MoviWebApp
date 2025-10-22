from fuzzywuzzy import fuzz
import re
import wikipedia as wiki

wiki.set_lang("de")


def get_random_page_and_content_snippet():
    while True:
        try:
            random_title = wiki.random(pages=1)
            page = wiki.page(random_title, auto_suggest=False)

            if page.content:
                lines = page.content.split('\n')
                snippet = "\n".join(lines[:11])
                snippet_2 = "\n".join(lines[11:30])

                title_pattern = re.compile(re.escape(random_title), re.IGNORECASE)
                cleaned_snippet = title_pattern.sub("...", snippet)
                cleaned_snippet_2 = title_pattern.sub("...", snippet_2)

                return page.title, cleaned_snippet, cleaned_snippet_2
        except (wiki.exceptions.PageError, wiki.exceptions.DisambiguationError,
                wiki.exceptions.RedirectError):
            continue


def play_game():
    print("Willkommen beim Wikipedia-Ratespiel! 🏃‍♂️")
    print("Beantworte Fragen richtig, um dein Männchen ins Ziel zu bringen.")


    track_length = 50 #  Gesamtlänge der Strecke
    man_position = 0   # Start spieler 1
    man_position_2 = 0 # start spieler 2
    player_1 = True
    player_2 = False

    if player_1 or player_2:

        while man_position < track_length or man_position_2 < track_length:
            print(f"\n--- DEIN FORTSCHRITT: {man_position}/{track_length} ---")

        # strecke

            track = "_" * man_position + "👨‍🦽‍➡️‍" + "_" * (track_length - man_position)
            print(track)
            track_2 = "_" * man_position_2 + "🧑‍🦼‍➡️️" + "_" * (track_length - man_position_2)
            print(track_2)

            title, content_snippet,content_snippet_two = get_random_page_and_content_snippet()

            guesses_left = 3
            correctly_guessed = False


            print("\nHinweis:")
            print(content_snippet)


            while guesses_left > 0 and not correctly_guessed:
                guess = input(f"Versuch {4 - guesses_left}: Was ist der Suchbegriff? ").strip()

                if fuzz.ratio(guess.lower(), title.lower()) >= 70:
                    print(f"🎉 Richtig! Du hast '{title}' erraten!")
                    if  player_1:
                        if guesses_left == 3:
                            man_position += 10  # Männchen läuft 10 Einheiten vorwärts
                        elif guesses_left == 2:
                            man_position += 5
                        elif guesses_left == 1:
                            man_position += 3
                        correctly_guessed = True
                        player_1 = False
                        player_2 = True

                    elif player_2:
                        if guesses_left == 3:
                            man_position_2 += 10  # Männchen läuft 10 Einheiten vorwärts
                        elif guesses_left == 2:
                            man_position_2 += 5
                        elif guesses_left == 1:
                            man_position_2 += 3
                        correctly_guessed = True
                        player_1 = True
                        player_2 = False
                else:
                    guesses_left -= 1
                    print("Leider falsch.")

                    if guesses_left == 2:
                        print(f"Hinweis 2: '{content_snippet_two}'.")
                    elif guesses_left == 1:
                        #Alternativer Hinweis für den letzten Versuch
                        print(f"Hinweis 3: der erste Buchstabe begint mit einem : {title[0]}")

            if not correctly_guessed:
                if player_1:
                    player_1 = False
                    player_2 = True
                else:
                    player_2 = False
                    player_1 = True

                print(f"Die Runde ist vorbei. Die richtige Antwort war: {title}")

        print("\n--- SPIEL BEENDET ---")
        print("🎉 Glückwunsch! Dein Männchen hat das Ziel erreicht! 🎉")
        if man_position >= track_length:
            print("Spieler 1 hat gewonnen! Whoohoohoo 🐋💨 !!!")
        if man_position_2 >= track_length:
            print("Spieler 2 hat gewonnen! Whoohoohoo 🐳💨 !!!")

if __name__ == "__main__":
    play_game()