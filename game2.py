import re
import json
import random
from player_module import Player
from game_functions import guess

players = []

with open('result.json') as fp:
    data = json.load(fp)

years = list(data.keys())

# setup game
i = 1
while True:
    print("Type in name of player " + str(i))
    new_player = input()
    players.append(Player(new_player, years))
    print()
    inpt = input("Do you wish to add another player? (y/n)\n")
    print()
    if "y" in inpt:
        i = i + 1
        continue
    else:
        break
print()

print("Current players:")
for player in players:
    print(player.name)
print()
print("Let the games begin!")

turn = 0
while True:

    # present the player and their years
    player = players[turn % len(players)]
    print("Current player: " + player.name)
    for year in player.years:
        print(year)
    print()

    # Get the year and question
    year = random.choice(player.year_data)
    events = data[year]
    event = random.choice(events)
    events.remove(event)
    data[year] = events
    event = re.sub(r'([ ]?)(\d{4})([ \.,])', r'\1[censored]\3', event)
    correct_year = int(year)
    # present the event and wait for answer
    print("Event:")
    print(event)
    print()
    print("Guess the year:")
    guessed_year = int(input())
    print()

    # calculate if it's correct or not
    correct = False

    if not player.years:
        correct = True
    elif len(player.years) == 1:
        have_year = int(player.years[0])
        wrong1 = guessed_year < have_year and correct_year > have_year
        wrong2 = correct_year < have_year and guessed_year > have_year
        if not (wrong1 or wrong2):
            correct = True
    else:
        correct = guess(guessed_year, correct_year, player.years)

    # present win-message or loose-message and handle the data
    if correct:
        print("Correct! The event transpired in " + year)
        player.years.append(correct_year)
        # remove the year from players pool of possible years
        player.year_data.remove(year)
    else:
        print("Unfortunately that's wrong, the event transpired in " + year)
        # Switch to next player
    turn += 1
    print()
