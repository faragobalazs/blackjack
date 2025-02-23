'''This is a more complicated, but not full version of Blackjack Game simulator.'''

from art import logo
import random

cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

players_cards = []
computers_cards = []

players_total = 0
computers_total = 0

# ----------------------------------------------------------------------------------------- #

def gamblers_next_card():
    return random.choice(cards)

def dealers_next_card():
    return random.choice(cards)

def sum_player(player):
    global players_total
    players_cards.append(player)
    players_total = sum(players_cards)

def sum_computer(computer):
    global computers_total
    computers_cards.append(computer)
    computers_total = sum(computers_cards)

def current_score_board(players_cards, computers_cards, players_total):
    print(f"\n🤠 Your cards: {players_cards}, current score: {players_total}")
    print(f"🤖 Computer's first card: {computers_cards[0]}")

def final_score_board(players_cards, computers_cards, players_total, computers_total):
    print(f"🤠 Your cards: {players_cards}, current score: {players_total}")
    print(f"🤖 Computer's cards: {computers_cards}, current score: {computers_total}")

def blackjack_player(players_total):
    if players_total == 21:
        print("\n***** Player's got Blackjack! PLAYER WON! 🤩 *****")
        final_score_board(players_cards, computers_cards, players_total, computers_total)
        outro()
    else:
        pass

def blackjack_computer(computers_total):
    if computers_total == 21:
        print("\n***** Computer's got Blackjack! COMPUTER WON! 😭 *****")
        outro()
    else:
        pass

def over_21_player():
    global players_total
    global players_cards
    if players_total > 21:
        if 11 in players_cards:
            print("Player's total score is above 21, but the Ace counts as 1 instead of 11.")
            players_cards.remove(11)
            players_cards.append(1)
            players_total = sum(players_cards)
        else:
            print("***** Player's total score is above 21. COMPUTER WON! 😭 *****")
            final_score_board(players_cards, computers_cards, players_total, computers_total)
            outro()

def first_two_cards():
    global players_total
    players_next_card = gamblers_next_card()
    computers_next_card = dealers_next_card()
    sum_player(players_next_card)
    sum_computer(computers_next_card)
    players_next_card = gamblers_next_card()
    computers_next_card = dealers_next_card()
    sum_player(players_next_card)
    sum_computer(computers_next_card)
    blackjack_player(players_total)
    blackjack_computer(computers_total)
    over_21_player()
    current_score_board(players_cards, computers_cards, players_total)

def players_round():
    second_question = input("\nType 'y' to get another card, type 'n' to pass: ")
    if second_question == "y":
        global players_total
        players_next_card = gamblers_next_card()
        sum_player(players_next_card)
        blackjack_player(players_total)
        current_score_board(players_cards, computers_cards, players_total)
        over_21_player()
        current_score_board(players_cards, computers_cards, players_total)
        players_round()
    else:
        pass

def computers_round():
    global players_total
    global computers_total
    if computers_total < 17:
        computers_next_card = dealers_next_card()
        sum_computer(computers_next_card)
        blackjack_computer(computers_total)
        computers_round()
    elif computers_total > 21:
        print("\n***** Computer's total score is above 21. PLAYER WON! 🤩 *****")
        final_score_board(players_cards, computers_cards, players_total, computers_total)
        outro()
    else: # 17 <= computers_total <= 21
        if players_total > computers_total:
            print("\n***** PLAYER WON! 🤩 *****")
            final_score_board(players_cards, computers_cards, players_total, computers_total)
        elif players_total < computers_total:
            print("\n***** COMPUTER WON! 😭 *****")
            final_score_board(players_cards, computers_cards, players_total, computers_total)
        else:
            print("\n***** IT IS A DRAW! 🙃 *****")
            final_score_board(players_cards, computers_cards, players_total, computers_total)

def intro():
    print(logo)
    first_question = input("\nDo you want to play a game of Blackjack ♠️♥️♣️♦️? Type 'y' or 'n': ")
    if first_question == "y":
        gameplay()
    else:
        print("\nMaybe next time. Good Bye. 👋")
        exit()

def outro():
    global players_cards
    global computers_cards
    global players_total
    global computers_total
    first_question = input("\nDo you want to play a game of Blackjack ♠️♥️♣️♦️? Type 'y' or 'n': ")
    if first_question == "y":
        print("\n" * 100)
        print(logo)
        players_cards = []
        computers_cards = []
        players_total = 0
        computers_total = 0
        gameplay()
    else:
        print("\nThank you for playing. Good Bye. 👋")
        exit()

def gameplay():
    first_two_cards()
    players_round()
    computers_round()
    outro()

# ----------------------------------------------------------------------------------------- #

intro()
gameplay()

# ----------------------------------------------------------------------------------------- #
# End of Code