'''This is a simple version of Blackjack Game simulator.'''

from art import logo
import random

# ------------------------------------------------------------------------------------------------- #

cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

players_cards = []
computers_cards = []

players_total = 0
computers_total = 0

# ------------------------------------------------------------------------------------------------- #

def gamblers_next_card():
    global players_total
    players_next_card = random.choice(cards)
    players_cards.append(players_next_card)
    players_total = sum(players_cards)

def dealers_next_card():
    global computers_total
    if computers_total <= 17:
        computers_next_card = random.choice(cards)
        computers_cards.append(computers_next_card)
        computers_total = sum(computers_cards)
    else:
        pass

def current_score_board(players_cards, computers_cards):
    print(f"\n🤠 Your cards: {players_cards}, current score: {players_total}")
    print(f"🤖 Computer's cards: {computers_cards}, current score: {computers_total}")

def final_score_board(players_cards, computers_cards):
    print(f"\n🤠 Your cards: {players_cards}, final score: {players_total}")
    print(f"🤖 Computer's cards: {computers_cards}, final score: {computers_total}")

def blackjack(players_total, computers_total):
    if players_total == 21:
        print("\nPlayer's got Blackjack!")
        print("***** PLAYER WON! *****")
        exit()
    elif computers_total == 21:
        print("\nDealer's got Blackjack!")
        print("***** DEALER WON! *****")
        exit()
    elif players_total > 21:
        print("\nPlayer's total score is over 21.")
        print("***** DEALER WON! *****")
        exit()
    elif computers_total > 21:
        print("\nDealer's total score is over 21.")
        print("***** PLAYER WON! *****")
        exit()
    else:
        print(" ")

def results():
    global players_total
    global computers_total
    if players_total > computers_total:
        final_score_board(players_cards, computers_cards)
        print("\n***** PLAYER WON! *****")
        exit()
    elif players_total < computers_total:
        final_score_board(players_cards, computers_cards)
        print("\n***** DEALER WON! *****")
        exit()
    else:
        final_score_board(players_cards, computers_cards)
        print("\n***** IT IS A DRAW! *****")
        exit()

def intro():
    print(logo)
    first_question = input("\nDo you want to play a game of Blackjack ♠️♥️♣️♦️? Type 'y' or 'n': ")
    if first_question == "y":
        gamblers_next_card()
        dealers_next_card()
        current_score_board(players_cards, computers_cards)
        blackjack(players_total, computers_total)
    else:
        print("\nThank you for playing. Good Bye.")
        exit()

def next_round():
    second_question = input("\nType 'y' to get another card, type 'n' to pass: ")
    if second_question == "y":
        gamblers_next_card()
        current_score_board(players_cards, computers_cards)
        blackjack(players_total, computers_total)
        dealers_next_card()
        current_score_board(players_cards, computers_cards)
        blackjack(players_total, computers_total)
        current_score_board(players_cards, computers_cards)
    elif second_question == "n":
        dealers_next_card()
        blackjack(players_total, computers_total)
        dealers_next_card()
        blackjack(players_total, computers_total)
        current_score_board(players_cards, computers_cards)
        results()
    else:
        next_round()

def turn_off():
    last_question = input("Do you want to play a game of Blackjack ♠️♥️♣️♦️? Type 'y' to play, or 'n' to exit.")
    if last_question == "y":
        intro()
    elif last_question == "n":
        print("\nThank you for playing. Good Bye.")
        exit()
    else:
        turn_off()

# ------------------------------------------------------------------------------------------------- #

intro()      # 1st ROUND
next_round() # 2nd ROUND
next_round() # 3rd ROUND
next_round() # 4th ROUND

# ------------------------------------------------------------------------------------------------- #
# End of Code