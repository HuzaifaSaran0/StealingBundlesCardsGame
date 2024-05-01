import tkinter as tk
from tkinter import messagebox
import random


class CardGame:
    def __init__(self, master):
        self.master = master
        self.master.title("Card Game")

        self.p1, self.p2, self.p3, self.p4 = [], [], [], []
        self.screen_cards = []
        self.players = [self.p1, self.p2, self.p3, self.p4]
        self.distributions = 1
        self.dealer_cards = ["A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K"] * 4

        self.initialize_game()

    def initialize_game(self):
        self.screen_cards_distribution()
        self.dealer_card_distribution()
        self.current_player = 0
        self.game_started = True

        self.create_widgets()
        self.update_display()

    def screen_cards_distribution(self):
        for _ in range(4):
            index = random.randint(0, len(self.dealer_cards) - 1)
            s_card = self.dealer_cards.pop(index)
            self.screen_cards.append(s_card)

    def dealer_card_distribution(self):
        for the_card in range(4):
            for _ in range(4):
                value_removed = random.randint(0, len(self.dealer_cards) - 1)
                card = self.dealer_cards.pop(value_removed)
                self.players[the_card].append(card)

    def match_card(self, card):
        if card in self.players[self.current_player]:
            removed_card = card
            self.players[self.current_player].remove(card)
            if removed_card in self.screen_cards:
                self.screen_cards.remove(removed_card)
                self.screen_removed_card = removed_card
                self.players[self.current_player].extend([self.screen_removed_card, removed_card])
                self.screen_cards.append(removed_card)
            else:
                self.screen_cards.append(removed_card)
            self.current_player = (self.current_player + 1) % 4
            self.update_display()
            if all(not self.players[player] for player in range(4)):
                self.game_over()
        else:
            messagebox.showinfo("Invalid Card", "You don't have this card. Try again.")

    def update_display(self):
        self.screen_cards_label.config(text="Screen Cards: " + " ".join(self.screen_cards))
        self.current_player_label.config(text="Player " + str(self.current_player + 1) + "'s Turn")
        self.players_cards_label.config(text="Your cards: " + " ".join(self.players[self.current_player]))

    def game_over(self):
        messagebox.showinfo("Game Over", "All players have run out of cards!")
        self.master.destroy()

    def create_widgets(self):
        self.screen_cards_label = tk.Label(self.master, text="Screen Cards: " + " ".join(self.screen_cards),
                                           font=("Helvetica", 12))
        self.screen_cards_label.pack()

        self.current_player_label = tk.Label(self.master, text="Player " + str(self.current_player + 1) + "'s Turn",
                                             font=("Helvetica", 12))
        self.current_player_label.pack()

        self.players_cards_label = tk.Label(self.master,
                                            text="Your cards: " + " ".join(self.players[self.current_player]),
                                            font=("Helvetica", 12))
        self.players_cards_label.pack()

        self.card_entry = tk.Entry(self.master)
        self.card_entry.pack()

        self.play_button = tk.Button(self.master, text="Play Card", command=self.play_card)
        self.play_button.pack()

    def play_card(self):
        card = self.card_entry.get().strip().upper()
        self.card_entry.delete(0, tk.END)
        self.match_card(card)


def main():
    root = tk.Tk()
    app = CardGame(root)
    root.mainloop()


if __name__ == "__main__":
    main()
