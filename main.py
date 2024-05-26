import random


class Card_stealing_game:
    def __init__(self):
        # Initialize player hands and piles
        self.p1, self.p2, self.p3, self.p4 = [], [], [], []
        self.pile1, self.pile2, self.pile3, self.pile4 = [], [], [], []
        self.screen_cards = []
        self.players = [self.p1, self.p2, self.p3, self.p4]
        self.piles = [self.pile1, self.pile2, self.pile3, self.pile4]
        self.pile_ending_cards_collection = []
        self.distributions = 1
        self.dealer_cards = ["A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K"] * 4
        self.match_condition = False  # Flag to indicate if a card has matched with screen cards or other player's piles
        # print(f"\n------Distribution number {self.distributions}------")
        self.screen_cards_distribution()
        self.dealer_Card_distribution()
        self.game_started = True
        while self.game_started:
            for the_player in self.players:
                if not self.distribution_condition_checking(the_player):
                    if self.distributions < 3:
                        self.dealer_Card_distribution()
                        self.distributions += 1
                        # print(f"\n------Distribution number {self.distributions}------")
                    else:
                        self.Game_over(self.players.index(the_player))

                # print(f"\n--------Player{self.players.index(the_player) + 1}'s Turn--------\n")
                # print(f"Your cards: {the_player}")
                # print(f"Screen cards: {self.screen_cards}")
                # for player in range(4):
                #     print(f"Player{player + 1} pile: {self.piles[player][-1] if self.piles[player] and not player
                #     == self.players.index(the_player) else []}")
                self.card_throw(self.players.index(the_player))  # Prompt the player to match a card from their
                # hand with a card on the screen

    # Function to distribute screen cards
    def screen_cards_distribution(self):
        for k in range(4):
            Index = random.randint(0, len(self.dealer_cards) - 1)
            s_card = self.dealer_cards.pop(Index)
            self.screen_cards.append(s_card)

    # Function to distribute cards to players
    def dealer_Card_distribution(self):
        for the_card in range(4):
            for j in range(4):
                value_removed = random.randint(0, len(self.dealer_cards) - 1)
                card = self.dealer_cards.pop(value_removed)
                self.players[the_card].append(card)

    # Function to handle card matching logic
    def match_card(self, card, player_number):
        if card in self.players[player_number]:
            removed_card = card
            self.players[player_number].remove(card)
            for index_number in range(4):
                self.match_condition = False
                for pile_card in range(4):
                    if self.piles[pile_card] or not self.piles[pile_card]:
                        if self.piles[pile_card]:
                            if removed_card == self.piles[pile_card][-1] and not player_number == pile_card:
                                self.piles[player_number].extend(self.piles[pile_card])
                                self.piles[player_number].append(removed_card)
                                self.piles[pile_card].clear()
                                self.match_condition = True
                                break
                        else:
                            continue
                if self.match_condition:
                    break
                if removed_card in self.screen_cards:
                    self.screen_cards.remove(removed_card)
                    Screen_removed_card = removed_card
                    self.piles[player_number].append(Screen_removed_card)
                    self.piles[player_number].append(removed_card)
                    self.match_condition = True
                    break
                else:
                    self.screen_cards.append(removed_card)
                    self.match_condition = True
                    break
        else:
            # print("Wrong Card Number, Throw Again:")
            self.card_throw(player_number)

    # Function to handle player's turn for throwing a card
    def card_throw(self, player_number):
        pass
        # card = input("Enter card number to throw a card:")
        # return self.card_through_type(card, player_number)

    # Function to handle input validation for card throwing
    def card_through_type(self, card, the_player_number):
        try:
            the_card = card.capitalize()
            return self.match_card(the_card, the_player_number)
        except TypeError:
            return self.match_card(str(card), the_player_number)

    # Function to check the condition for distribution
    def distribution_condition_checking(self, the_current_player):
        # PILE COLLECTION START
        if self.distributions < 3:
            for p in self.piles:
                if p:
                    if self.piles.index(p) == self.players.index(the_current_player):
                        self.pile_ending_cards_collection.append("")
                    else:
                        self.pile_ending_cards_collection.append(p[-1])
                else:
                    self.pile_ending_cards_collection.append("")
        # PILE COLLECTION END

        # CHECKING CARD MATCHING START
        for every_player in self.players:
            if every_player:
                self.pile_ending_cards_collection.clear()
                return True
        self.pile_ending_cards_collection.clear()
        return False

    # Function to handle end of the game
    def Game_over(self, index_of_last_player_matching):
        # print("------Game Over-------")
        self.piles[index_of_last_player_matching].extend(self.screen_cards)
        for i in range(4):
            self.piles[i].extend(self.players[i])
            self.players[i].clear()
        scores = []
        # print("------Scores-------")
        for scorer in self.piles:
            # print(f"Player {self.piles.index(scorer) + 1}: {len(scorer)}")
            scores.append(len(scorer))
        self.screen_cards.clear()
        # print(f"Winner is Player {scores.index(max(scores)) + 1}")
        exit()


# Start of the game

newGame = Card_stealing_game()
