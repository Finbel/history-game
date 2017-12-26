import json
import random
import re

from game_functions import guess
from screen_module import Screen
from player_module import Player


class Game(object):

    def __init__(self, screen):
        # The screen to which things are written
        self.screen = Screen(screen)
        self.players = []
        self.turn_number = 0

    def add_player(self, player_number, years):
        self.screen.message(
            "Welcome", "Type in the name of player " + str(player_number))
        player = input("*  > ")
        self.players.append(Player(player, years))
        self.screen.add_player(player)

    def startup(self):
        with open('result.json') as fp:
            self.data = json.load(fp)
        self.years = list(self.data.keys())
        player_number = 1
        while True:
            self.add_player(player_number, self.years)
            self.screen.message(
                "Welcome", "Do you wish to add another player? (y/n)")
            another = input("*  > ")
            if "y" in another:
                player_number += 1
                continue
            else:
                break

    def run(self):
        while(True):
            player = self.players[self.turn_number]
            self.screen.next_turn()

            events = []
            while len(events) < 1:
                year = random.choice(player.year_data)
                events = self.data[year]
            event = random.choice(events)
            events.remove(event)
            self.data[year] = events
            event = re.sub(r'\d{4}', r'[censored]', event)
            correct_year = int(year)
            self.screen.message("Event:", event, "Guess the year!")
            guessed_year = int(input("*  > "))
            correct = guess(guessed_year, correct_year, player.years)

            if correct:
                self.players[self.turn_number].years.append(correct_year)
                self.screen.add_year(player.name, year)
                self.screen.print_years()
                self.screen.message(
                    "Correct! You guessed " + str(guessed_year) + ".", "The event transpired in " + year)
                # remove the year from players pool of possible years
                self.players[self.turn_number].year_data.remove(year)
            else:
                self.screen.message(
                    "Unfortunately that's wrong", "the event transpired in " + year)
                # Switch to next player
            self.turn_number = (self.turn_number + 1) % len(self.players)
            input()
            print()
