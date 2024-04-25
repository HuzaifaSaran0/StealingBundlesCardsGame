import random
import time

cards = ["A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K"] * 4

p1 = []
p2 = []
p3 = []
p4 = []
cards_on_the_screen = []
distributions = 0
other_players_card = [[], [], [], []]  # Only those which were matched
# cards_on_the_screen = random.choices(cards, k=4)

players = [p1, p2, p3, p4]


def screen_card():
    for k in range(4):
        index = random.randint(0, len(cards) - 1)
        s_card = cards.pop(index)
        cards_on_the_screen.append(s_card)


def dealer_Card_distribution():
    for i in range(4):
        # players[i].clear()
        for j in range(4):
            index = random.randint(0, len(cards) - 1)
            card = cards.pop(index)
            players[i].append(card)


def Type(value_to_check_type, value_index):
    try:
        int_value = int(value_to_check_type)
        Match(int_value, value_index)
    except ValueError:
        Match(value_to_check_type.capitalize(), value_index)


def Match(thrown, index):
    if thrown in cards_on_the_screen:
        removed_card = thrown
        cards_on_the_screen.remove(thrown)
        players[index - 1].append(removed_card)
        other_players_card[index].append(removed_card)

    elif thrown in other_players_card[index]:
        # removed_card = thrown
        # other_players_card[index].remove(thrown)
        removed_card = To_remove_from_other_players_cards(thrown, index)
        players[index - 1].append(removed_card)
    else:
        cards_on_the_screen.append(thrown)


def To_remove_from_other_players_cards(value, index_no):
    for i in other_players_card:
        if i != index_no:
            for j in i:
                if value == j:
                    the_removed_value = value
                    other_players_card[j].remove(value)
                    return the_removed_value


# dealer_Card_distribution()  # Throw1
screen_card()
while cards != 0:
    # if (p1 == [] or p2 == [] or p3 == [] or p4 == [])
    if distributions < 3:
        time.sleep(1)
        print(f"\n\n----------Distribution # {distributions + 1}----------\n\n")
        dealer_Card_distribution()
        distributions += 1

    for player_input in range(4):
        print(f"\n\n-----Player {player_input + 1} Turn-----")
        if players[player_input]:
            print(f"Player{player_input + 1}'s Cards = {players[player_input]}")
            print(f"Screen Cards = {cards_on_the_screen}")
            print(f"Other Player's Cards = {other_players_card}")
            thrown_number = input("Write Card Number to match:")
            Type(thrown_number, player_input + 1)
            time.sleep(1)
        #     Call the function to check if it matches or not
        #     if match :
        #     print("----- MATCH -----")
        #     else:
        #     print("----- PASS -----")


