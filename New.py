import random

# Initialize player hands and piles
p1, p2, p3, p4 = [], [], [], []
pile1, pile2, pile3, pile4 = [], [], [], []
screen_cards = []
players = [p1, p2, p3, p4]
piles = [pile1, pile2, pile3, pile4]
pile_ending_cards_collection = []
distributions = 1
dealer_cards = ["A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K"] * 4
match_condition = False  # Flag to indicate if a card has matched with screen cards or other player's piles


# Function to distribute screen cards
def screen_cards_distribution():
    for k in range(4):
        Index = random.randint(0, len(dealer_cards) - 1)
        s_card = dealer_cards.pop(Index)
        screen_cards.append(s_card)


# Function to distribute cards to players
def dealer_Card_distribution():
    for the_card in range(4):
        for j in range(4):
            value_removed = random.randint(0, len(dealer_cards) - 1)
            card = dealer_cards.pop(value_removed)
            players[the_card].append(card)


# Function to handle card matching logic
def match_card(card, player_number):
    if card in players[player_number]:
        removed_card = card
        players[player_number].remove(card)
        for index_number in range(4):
            global match_condition
            match_condition = False
            for pile_card in range(4):
                if piles[pile_card] or not piles[pile_card]:
                    if piles[pile_card]:
                        if removed_card == piles[pile_card][-1] and not player_number == pile_card:
                            piles[player_number].extend(piles[pile_card])
                            piles[player_number].append(removed_card)
                            piles[pile_card].clear()
                            match_condition = True
                            break
                    else:
                        continue
            if match_condition:
                break
            if removed_card in screen_cards:
                screen_cards.remove(removed_card)
                Screen_removed_card = removed_card
                piles[player_number].append(Screen_removed_card)
                piles[player_number].append(removed_card)
                match_condition = True
                break
            else:
                screen_cards.append(removed_card)
                match_condition = True
                break
    else:
        print("Wrong Card Number, Throw Again:")
        card_throw(player_number)


# Function to handle player's turn for throwing a card
def card_throw(player_number):
    card = input("Enter card number to throw a card:")
    return card_through_type(card, player_number)


# Function to handle input validation for card throwing
def card_through_type(card, the_player_number):
    try:
        the_card = card.capitalize()
        return match_card(the_card, the_player_number)
    except TypeError:
        return match_card(str(card), the_player_number)


# Function to check the condition for distribution
def distribution_condition_checking(the_current_player):
    # PILE COLLECTION START
    if distributions < 3:
        for p in piles:
            if p:
                if piles.index(p) == players.index(the_current_player):
                    pile_ending_cards_collection.append("")
                else:
                    pile_ending_cards_collection.append(p[-1])
            else:
                pile_ending_cards_collection.append("")
    # PILE COLLECTION END

    # CHECKING CARD MATCHING START
    for every_player in players:
        if every_player:
            pile_ending_cards_collection.clear()
            return True
    pile_ending_cards_collection.clear()
    return False


# Function to handle playing again
# def play_again():
#     choice = input("Wanna Play Again??(yes/no):")
#     if choice.upper() == "YES":
#         return True
#     else:
#         return False


# Function to handle end of the game
def Game_over(index_of_last_player_matching):
    print("------Game Over-------")
    piles[index_of_last_player_matching].extend(screen_cards)
    for i in range(4):
        piles[i].extend(players[i])
        players[i].clear()
    scores = []
    print("------Scores-------")
    for scorer in piles:
        print(f"Player {piles.index(scorer) + 1}: {len(scorer)}")
        scores.append(len(scorer))
    screen_cards.clear()
    print(f"Winner is Player {scores.index(max(scores)) + 1}")
    exit()


# Start of the game
print(f"\n------Distribution number {distributions}------")
screen_cards_distribution()
dealer_Card_distribution()

game_started = True
while game_started:
    for the_player in players:
        if not distribution_condition_checking(the_player):
            if distributions < 3:
                dealer_Card_distribution()
                distributions += 1
                print(f"\n------Distribution number {distributions}------")
            else:
                Game_over(players.index(the_player))

        print(f"\n--------Player{players.index(the_player) + 1}'s Turn--------\n")
        print(f"Your cards: {the_player}")
        print(f"Screen cards: {screen_cards}")
        for player in range(4):
            print(f"Player{player + 1} pile: "
                  f"{piles[player][-1] if piles[player] and not player == players.index(the_player) else []}")
        card_throw(players.index(the_player))
