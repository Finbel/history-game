

class Screen(object):

    def __init__(self, screen_file):
        # The screen to which things are written
        self.screen_file = screen_file
        self.players = []
        self.player_years = {}
        self.current_player = -1
        self.message_list = ["*  \n"]
        self.message_height = 0
        self.title_line = 8
        self.message_line = 9
        self.prompt_line = 11
        self.title = "*  \n"
        self.prompt = "*  \n"
        self.top_score = 0
        self.setup()

    def setup(self):
        lines = []

        lines.append("*" * 80 + "\n")
        for i in range(1, 20):
            lines.append("*  \n")

        with open(self.screen_file, 'w+') as file:
            file.writelines(lines)

    def add_player(self, player):
        self.players.append(player)
        self.player_years[player] = []
        self.print_players()

    def next_turn(self):
        self.current_player = (self.current_player + 1) % len(self.players)
        with open(self.screen_file, 'r') as file:
            lines = file.readlines()

        truncate = ""
        if self.current_player:
            for i in range(self.current_player):
                truncate += (" " * len(self.players[i])) + "  "
        lines[1] = "*  " + truncate + "~***~\n"

        with open(self.screen_file, 'w') as file:
            file.writelines(lines)

    def add_year(self, player, year):
        years = self.player_years[player]
        years.append(year)
        years.sort()
        self.player_years[player] = years

        scores = [len(years) for years in list(self.player_years.values())]
        self.top_score = max(scores)
        if self.top_score > 4:
            self.title_line = self.top_score + 4
            self.message_line = self.title_line + 1
            self.prompt_line = self.message_line + self.message_height + 2

    def print(self):
        self.print_message()
        for i in range(30):
            print()
        with open(self.screen_file, 'r') as file:
            lines = file.readlines()
        for line in lines:
            print(line, end="")

    def print_players(self):
        with open(self.screen_file, 'r') as file:
            lines = file.readlines()

        player_index = 3
        player_string = "*  "
        for i in range(len(self.players)):
            player_string += self.players[i] + "  "
        lines[2] = player_string + "\n"

        with open(self.screen_file, 'w') as file:
            file.writelines(lines)

    def print_years(self):

        with open(self.screen_file, 'r') as file:
            lines = file.readlines()

        for line_index in range(3, 4 + self.top_score):
            lines[line_index] = "*  "

        for player_index in range(len(self.players)):
            for line_index in range(3, 3 + self.top_score):
                try:
                    lines[line_index] += str(self.player_years[self.players[player_index]
                                                               ][line_index - 3])
                except IndexError:
                    lines[line_index] += "    "
                lines[line_index] += " " * \
                    (len(self.players[player_index]) - 2)

        for line_index in range(3, 4 + self.top_score):
            lines[line_index] += "\n"

        with open(self.screen_file, 'w') as file:
            file.writelines(lines)

    def remove_message(self):
        with open(self.screen_file, 'r') as file:
            lines = file.readlines()
        if self.message_height:
            i = 0
            while i < len(lines)-self.title_line:
                lines[self.title_line + i] = "*  \n"
                i += 1
        with open(self.screen_file, 'w') as file:
            file.writelines(lines)

    def message(self, title, message, prompt = None):
        self.title = "*  " + title + "\n"
        if prompt is not None:
            self.prompt = "*  ~~ " + prompt + "\n"
        else:
            self.prompt = "*  \n"
        message_array = message.split(" ")
        length = 0
        self.message_height = 1
        line_list = []
        line = ""
        for i in range(len(message_array)):
            if length > 60:
                line_list.append("*  " + line + "\n")
                line = message_array[i] + " "
                self.message_height += 1
                length = 0
            else:
                line += message_array[i] + " "
                length += len(message_array[i]) + 1
        line_list.append("*  " + line + "\n")
        self.message_list = line_list
        self.prompt_line = self.message_line + self.message_height + 2
        self.print_message()
        self.print()

    def print_message(self):
        self.remove_message()
        with open(self.screen_file, 'r') as file:
            lines = file.readlines()

        lines[self.title_line] = self.title

        message = self.message_list

        for i in range(len(message)):
            lines[self.message_line + i] = message[i]

        lines[self.prompt_line] = self.prompt

        with open(self.screen_file, 'w') as file:
            file.writelines(lines)
