from board import Board
import random

# ANSI-Farbcodes
COLOR_CODES = {
    "pink": "\033[95m",
    "hellblau": "\033[96m",
    "rot": "\033[91m",
    "grün": "\033[92m",
    "gelb": "\033[93m",
    "blau": "\033[94m",
    "endc": "\033[0m"
}

# Spielerklasse
class Player:
    def __init__(self, symbol, is_computer=False):
        self.symbol = symbol
        self.is_computer = is_computer
        if not is_computer:
            self.name = input(f"Gib den Namen für Spieler {symbol} ein: ")
            color = input(f"{self.name}, welche Farbe möchtest du für dein Symbol? "
                          "(pink/hellblau/rot/grün/gelb/blau): ").lower()
        else:
            self.name = "Computer"
            color = "blau"  # Computerfarbe
        self.color = COLOR_CODES.get(color, COLOR_CODES["pink"])

# Spielklasse
class TicTacToeGame:
    def __init__(self):
        self.board = Board()
        # Spieler X = Mensch, Spieler O = Computer
        self.player_X = Player("X")
        self.player_O = Player("O", is_computer=True)
        self.current_player = self.player_X

    def switch_player(self):
        self.current_player = self.player_O if self.current_player == self.player_X else self.player_X

    def colored_symbol(self, symbol, color):
        if symbol == "X":
           return f"{color}{symbol}{COLOR_CODES['endc']}"
        elif symbol == "O":
           return f"{color}{symbol}{COLOR_CODES['endc']}"
        else:
            return symbol

    def display_board(self):
        for row in self.board.grid:
            row_display = []
            for cell in row:
                if cell == "X":
                    row_display.append(self.colored_symbol("X", self.player_X.color))
                elif cell == "O":
                    row_display.append(self.colored_symbol("O", self.player_O.color))
                else:
                    row_display.append(" ")
            print(" " + " | ".join(row_display))
            print("---+---+---")

    def play_turn(self):
        print(f"\n{self.current_player.name} ({self.current_player.symbol}) ist am Zug!")

        if self.current_player.is_computer:
            # Computer wählt zufälliges freies Feld
            empty_cells = [(r, c) for r in range(3) for c in range(3) if self.board.grid[r][c] == " "]
            row, col = random.choice(empty_cells)
            print(f"Computer wählt Zeile {row}, Spalte {col}")
        else:
            try:
                row = int(input("Zeile eingeben (0–2): "))
                col = int(input("Spalte eingeben (0–2): "))
            except ValueError:
                print("⚠️ Bitte nur Zahlen von 0 bis 2 eingeben!")
                return False

        if not self.board.make_move(row, col, self.current_player.symbol):
            print("❌ Ungültiger Zug! Feld besetzt oder außerhalb des Spielfelds.")
            return False

        print("\nAktuelles Spielfeld:")
        self.display_board()
        return True

    def check_game_over(self):
        symbol = self.current_player.symbol
        if self.board.check_winner(symbol):
            print(f"🎉 {self.current_player.name} hat gewonnen!")
            return True
        elif self.board.is_full():
            print("🤝 Unentschieden! Niemand hat gewonnen.")
            return True
        return False

    def start_game(self):
        print("🎮 Willkommen bei Tic Tac Toe – Spieler vs Computer ✨💎")
        self.display_board()

        game_over = False
        while not game_over:
            move_made = self.play_turn()
            if move_made:
                game_over = self.check_game_over()
                if not game_over:
                    self.switch_player()

        print("\n🏁 Spiel beendet – danke fürs Spielen, Fee! 💖")

# Spiel starten
if __name__ == "__main__":
    game = TicTacToeGame()
    game.start_game()
