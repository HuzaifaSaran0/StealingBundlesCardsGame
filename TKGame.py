import random
from tkinter import *
from tkinter import messagebox
from PIL import Image, ImageTk

tkinter = Tk()
tkinter.title("Card Stealing Game")
screen_width = tkinter.winfo_screenwidth()
screen_height = tkinter.winfo_screenheight()
tkinter.geometry(f"{screen_width}x{screen_height}")

# Background Image Handling
bg_image = Image.open("bg.png")
bg_image = bg_image.resize((tkinter.winfo_screenwidth(), tkinter.winfo_screenheight()))
background = ImageTk.PhotoImage(bg_image)
image = Label(tkinter, image=background)
image.place(x=0, y=0, relwidth=1, relheight=1)

# List to store card widgets
card_widgets = []
game_condition = True
start_UpperA = 300
start_UpperB = 130
start_ScreenA = 300
start_ScreenB = 330
start_othersA = 300
start_othersB = 530

dealer_cards = ["A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K"] * 4
player1 = []
player2 = []
player3 = []
player4 = []
screen_cards = []
pile1 = []
pile2 = []
pile3 = []
pile4 = []
last_cards = []
piles = [pile1, pile2, pile3, pile4]
players = [player1, player2, player3, player4]
distributions = 1
scoreboard_window = Toplevel()
scoreboard_window.destroy()
play_again_BTN = Button()
# pile_ending_cards_collection = []


# Card Image
def card_generation(x, y, text):
    if text:
        card = Image.open("card.png")
        card = card.resize((100, 150))
        card = ImageTk.PhotoImage(card)
        card_image = Label(tkinter, image=card)
        card_image.card = card  # Keep a reference to the image to prevent garbage collection
        card_image.place(x=x, y=y)
        label = Label(tkinter, text=f"{text}", bg="light Grey", fg="black", font=("Arial", 14, "bold"))
        label.place(x=x + 5, y=y + 5)
        card_widgets.append((card_image, label))  # Store references to the widgets


def screen_cards_distribution():
    for i in range(4):
        index = random.randint(0, len(dealer_cards) - 1)
        s_card = dealer_cards.pop(index)
        screen_cards.append(s_card)


def card_distribution():
    for the_card in range(4):
        for j in range(4):
            value_removed = random.randint(0, len(dealer_cards) - 1)
            card = dealer_cards.pop(value_removed)
            players[the_card].append(card)


def input_card(callback):
    input_window = Toplevel(tkinter)
    input_window.title("Input Card")
    # TO MAKE UNABLE THE USER TO CLOSE THE WINDOW
    input_window.protocol("WM_DELETE_WINDOW", lambda: None)
    # TO MAKE UNABLE THE USER TO RESIZE THE WINDOW
    input_window.resizable(False, False)
    label = Label(input_window, text="Enter card to throw:", font=("Arial", 14))
    # THE APPEARANCE OF THE WINDOW ON THE SCREEN (X,Y)
    input_window.geometry("+50+50")
    label.pack(pady=10)

    entry = Entry(input_window, font=("Arial", 14))
    entry.pack(pady=10)
    entry.focus_set()

    def submit():
        user_input = entry.get()
        if user_input:
            input_window.destroy()
            callback(user_input)

    submit_button = Button(input_window, text="Submit", font=("Arial", 12), bg="light blue", command=submit)
    submit_button.pack(pady=10)
    # Bind the Enter key to the submit function
    input_window.bind('<Return>', lambda event: submit())


def hide_cards():
    for card_image, label in card_widgets:
        card_image.place_forget()
        label.place_forget()
    card_widgets.clear()  # Clear the list after hiding the cards


def Player_turn(player_number):
    label = Label(tkinter, text=f"Player {player_number + 1}'s Turn", bg="light Green", fg="black",
                  font=("Arial", 14, "bold"))
    label.place(x=300, y=50)


def last_cards_collection(player_num):
    last_cards.clear()
    for pile in piles:
        if pile:
            if piles.index(pile) == player_num:
                last_cards.append("")
            else:
                last_cards.append(pile[-1])
        else:
            last_cards.append("")
    # print(last_cards)


def player_cards(player_number):
    global start_UpperA, start_ScreenA
    labels()
    hide_cards()  # Hide the previous player's cards

    last_cards_collection(player_number)
    # Show the last card of each other player's stack
    for m, pile in enumerate(piles):
        if pile:
            if player_number != m:
                last_cards.append("")
                last_card = pile[-1]
                card_generation(start_othersA + 120 * m, start_othersB, last_card)
    for k in screen_cards:
        card_generation(start_ScreenA, start_ScreenB, k)
        start_ScreenA += 50
    start_ScreenA = 300
    for j, card in enumerate(players[player_number]):
        Player_turn(player_number)
        card_generation(start_UpperA + 50 * j, start_UpperB, card)
    start_UpperA = 300


def next_player(player_number):
    global distributions, game_condition
    if distributions < 3:
        if not distribution_condition_checking():
            distributions += 1
            card_distribution()
            print("Distribution number", distributions, "Done")
            last_cards_collection(player_number)
    else:
        if not distribution_condition_checking():
            for i in range(4):
                if players[i]:
                    piles[i].extend(players[i])
            if screen_cards:
                piles[player_number - 1].extend(screen_cards)
            endgame()
    if not game_condition:
        return
    player_number = player_number % len(players)  # Loop back to the first player
    player_cards(player_number)
    input_card(lambda user_input: match_card(user_input, player_number))


def labels():
    your_cards_label = Label(tkinter, text="Your Cards", bg="light Green", fg="black", font=("Arial", 14, "bold"))
    your_cards_label.place(x=50, y=200)
    screen_cards_label = Label(tkinter, text="Screen Cards", bg="light Green", fg="black", font=("Arial", 14, "bold"))
    screen_cards_label.place(x=50, y=400)
    other_players_cards_label = Label(tkinter, text="Cards Stacks", bg="light Green", fg="black",
                                      font=("Arial", 14, "bold"))
    other_players_cards_label.place(x=50, y=600)


def match_card(user_input, player_number):

    try:
        user_input = user_input.upper()  # Convert input to uppercase for case-insensitive matching
        if not user_input or user_input not in players[player_number]:
            messagebox.showerror("Invalid Input", "Please enter a valid card.")
            next_player(player_number)
        else:
            if user_input in players[player_number]:
                global last_cards
                if user_input in last_cards:
                    other_players_matching(user_input, player_number)
                    next_player(player_number + 1)
                elif user_input in screen_cards:
                    matching_effect(user_input, player_number)
                    next_player(player_number + 1)
                else:
                    # Your card has been added to the screen cards
                    not_matching(user_input, player_number)
                    next_player(player_number + 1)
                for i in range(4):
                    print(players[i])
                print("/n")
    except TypeError:
        next_player(player_number)


def distribution_condition_checking():
    # CHECKING CARD MATCHING START
    for every_player in players:
        for card in every_player:
            if card in screen_cards or card in last_cards:
                last_cards.clear()
                return True
    last_cards.clear()
    return False


def other_players_matching(the_input, player):
    for i in last_cards:
        if i == the_input:
            piles[player].extend(piles[last_cards.index(i)])
            piles[last_cards.index(i)].clear()
            matched_card = players[player].pop(players[player].index(the_input))
            piles[player].append(matched_card)  # for the player who matched the card
            break


def matching_effect(matched_card, player_number):
    screen_cards.remove(matched_card)
    players[player_number].remove(matched_card)
    other_player_number = player_number % len(players)  # Get the index of the other player
    piles[other_player_number].append(matched_card)  # Add the matched Screen card to the other player's pile
    piles[other_player_number].append(matched_card)  # Add the matched player's card to the other player's pile
    player_cards(player_number)  # Update player's cards on the screen


def not_matching(matched_card, player_number):
    players[player_number].remove(matched_card)
    screen_cards.append(matched_card)
    player_cards(player_number)  # Update player's cards on the screen


def start_game():
    start_game_button.destroy()
    next_player(0)


def show_scoreboard():
    global scoreboard_window
    play_again_game_button()
    scoreboard_window = Toplevel(tkinter)
    scoreboard_window.title("Scoreboard")
    scoreboard_window.protocol("WM_DELETE_WINDOW", lambda: None)
    scoreboard_window.resizable(False, False)
    scoreboard_window.geometry("+300+300")
    # Add labels to display scores for each player
    player_label = Label(scoreboard_window, text=f"SCORE BOARD", font=("Arial", 15, "bold"))
    player_label.pack()
    for i, player_score in enumerate(piles):
        player_label = Label(scoreboard_window, text=f"Player {i+1}: {len(player_score)}", font=("Arial", 13))
        player_label.pack()
    # Get the index of the pile with the most cards
    winner_index = max(range(len(piles)), key=lambda index: len(piles[index]))
    winner_label = Label(scoreboard_window, text=f"Winner: Player {winner_index + 1}", font=("Arial", 14))
    winner_label.pack()


def destroy_scoreBoard():
    global scoreboard_window
    scoreboard_window.destroy()


def play_again():
    global dealer_cards, player1, player2, player3, player4, screen_cards, pile1, pile2, pile3, pile4, last_cards, \
        piles, players, distributions, card_widgets, game_condition, scoreboard_window
    for widget in card_widgets:
        widget[0].destroy()
        widget[1].destroy()
    card_widgets = []
    destroy_scoreBoard()
    game_condition = True
    dealer_cards = ["A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K"] * 4
    player1 = []
    player2 = []
    player3 = []
    player4 = []
    screen_cards = []
    pile1 = []
    pile2 = []
    pile3 = []
    pile4 = []
    last_cards = []
    piles = [pile1, pile2, pile3, pile4]
    players = [player1, player2, player3, player4]
    distributions = 1
    screen_cards_distribution()
    card_distribution()
    next_player(0)
    destroy_play_again_button()


def play_again_game_button():
    global play_again_BTN
    play_again_BTN = Button(tkinter, text="Play Again", fg="white", border=5, bg="green", font=("Arial", 12, "bold"),
                            height=1, width=10, command=play_again)
    play_again_BTN.place(x=50, y=50)


def destroy_play_again_button():
    global play_again_BTN
    play_again_BTN.destroy()


def endgame():
    global game_condition
    game_condition = False
    show_scoreboard()


def exit_game():
    tkinter.destroy()


# Exit button
exit_button = Button(tkinter, text="Exit", fg="white", border=5, bg="red", font=("Arial", 12, "bold"),
                     height=1, width=10, command=exit_game)
exit_button.place(x=1000, y=50)

# Start the game button
screen_cards_distribution()
card_distribution()
start_game_button = Button(tkinter, text="Start Game", fg="white", border=5, bg="green", font=("Arial", 12, "bold"),
                           height=1, width=10, command=start_game)
start_game_button.place(x=50, y=50)
tkinter.mainloop()
