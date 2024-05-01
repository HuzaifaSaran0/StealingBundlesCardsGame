import random

p1, p2, p3, p4 = [], [], [], []
pile1, pile2, pile3, pile4 = [], [], [], []
screen_cards = []
players = [p1, p2, p3, p4]
piles = [pile1, pile2, pile3, pile4]
pile_ending_cards_collection = []
distributions = 1
dealer_cards = ["A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K"] * 4
match_condition = False  # That if the user player thrown card has matched with Screen_cards or other_piles cards or it


# is to throw in screen cards


def screen_cards_distribution():
    for k in range(4):
        Index = random.randint(0, len(dealer_cards) - 1)
        s_card = dealer_cards.pop(Index)
        screen_cards.append(s_card)


def dealer_Card_distribution():
    for the_card in range(4):  # for distributing cards to All 4 players
        for j in range(4):  # for distributing 4 cards to each player
            value_removed = random.randint(0, len(dealer_cards) - 1)
            card = dealer_cards.pop(value_removed)
            players[the_card].append(card)


def match_card(card, player_number):
    if card in players[player_number]:
        removed_card = card
        players[player_number].remove(card)
        for index_number in range(4):
            global match_condition
            match_condition = False
            for pile_card in range(4):
                if piles[pile_card] or not piles[pile_card]:  # To check If the pile is empty or not
                    if piles[pile_card]:
                        if removed_card == piles[pile_card][-1] and not player_number == pile_card:
                            piles[player_number].extend(piles[pile_card])
                            piles[player_number].append(removed_card)
                            piles[pile_card].clear()
                            print("You Matched The Card with other person's pile")
                            match_condition = True
                            break
                    else:
                        # print("continue HoGya")
                        continue
            if match_condition:
                break
            if removed_card in screen_cards:
                screen_cards.remove(removed_card)
                Screen_removed_card = removed_card
                piles[player_number].append(Screen_removed_card)
                piles[player_number].append(removed_card)
                print("You Matched The Card with Screen Cards")
                match_condition = True
                break
            else:
                print("You Threw The Card")
                screen_cards.append(removed_card)
                match_condition = True
                break
    else:
        print("Wrong Card Number, Throw Again:")
        card_throw(player_number)


def card_throw(player_number):
    card = input("Enter card number to throw a card:")
    return card_through_type(card, player_number)


def card_through_type(card, the_player_number):
    try:
        the_card = card.capitalize()
        return match_card(the_card, the_player_number)
    except TypeError:
        return match_card(str(card), the_player_number)


def distribution_condition_checking(the_current_player):
    # 1: PILE COLLECTION START
    if distributions < 3:
        for p in piles:
            if p:
                if piles.index(p) == players.index(the_current_player):
                    pile_ending_cards_collection.append("")
                else:
                    pile_ending_cards_collection.append(p[-1])
            else:
                pile_ending_cards_collection.append("")
    # 1: PILE COLLECTION END
    # 2: CHECKING CARD MATCHING START
    for every_player in players:
        if every_player:
            if set(every_player).intersection(set(screen_cards)) or set(every_player).intersection(
                    set(pile_ending_cards_collection)):
                print("True! You have a matching card")
                pile_ending_cards_collection.clear()
                return True
    print("False! No one has a matching card")
    pile_ending_cards_collection.clear()
    return False


def Game_over(index_of_last_player_matching):
    print("------Game Over-------")
    piles[index_of_last_player_matching].extend(screen_cards)
    # piles[index_of_last_player_matching].extend(players[index_of_last_player_matching])
    for i in range(4):
        piles[i].extend(players[i])
        players[i].clear()
    scores = []
    print("------Scores-------")
    for scorer in piles:
        print(f"Player {piles.index(scorer) + 1}: {len(scorer)}")
        scores.append(len(scorer))
    screen_cards.clear()
    print("Player 1 cards: ", p1)
    print("Player 2 cards: ", p2)
    print("Player 3 cards: ", p3)
    print("Player 4 cards: ", p4)
    print("Screen Cards: ", screen_cards)
    print(f"Pile Collection: {pile_ending_cards_collection}")

    print(f"Winner is Player {scores.index(max(scores)) + 1}")
    exit()


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
                # print("Game Over chl gyi hy bhai")
                Game_over(players.index(the_player))

        print(f"\n--------Player{players.index(the_player) + 1}'s Turn--------\n")
        print(f"Your cards: {the_player}")
        print(f"Screen cards: {screen_cards}")
        for player in range(4):  # For printing other players' piles without the player's own pile
            print(f"Player{player + 1} pile: "
                  f"{piles[player][-1] if piles[player] and not player == players.index(the_player) else []}")
        print("Player 1 cards: ", p1)
        print("Player 2 cards: ", p2)
        print("Player 3 cards: ", p3)
        print("Player 4 cards: ", p4)
        print("Screen Cards: ", screen_cards)
        print(f"Pile Collection: {pile_ending_cards_collection}")
        card_throw(players.index(the_player))


# for index, player_hand in enumerate(players):
# for i in range(4):
#     print(f"Player {i + 1} cards are: {players[i]}")
# print(f"Screen Cards are: {screen_cards}")
#
# print(dealer_cards)

#     if card not in players[player_number]:
#         return ValueError
#     return card
# except ValueError:
#     print("You don't have this card, Throw Again:")


# def input_card_plus_number_type(player_index_number):
#     the_thrown_card = card_throw(player_index_number)
#     try:
#         int_card = int(the_thrown_card)
#         return str(int_card)
#     except TypeError:
#         return the_thrown_card.capitalize()
#     # except ValueError:
#     #     input_card_plus_number_type(player_index_number)


# def card_match(card_user_throw, the_index):
#     if card_user_throw in screen_cards:
#         removed_card = card_user_throw
#         screen_cards.remove(card_user_throw)
#         piles[the_index].append(removed_card)
#     else:
#         screen_cards.append(card_user_throw)


# 1:Create a list of all last cards of the piles and if one don't have cards then an empty string in its last card place

# 2: In every player's turn check if ALL players have any card that is matching with Screen Cards or with any card
# in other players' piles
# If it is then make the next player to match/throw the card
# and if not matching any card of any player then play a new distribution of cards from the dealer
# and check the same for all players

