
class Player(object):

    def __init__(self, name, years):
        self.name = name
        # list of years guessed correctly
        self.years = []
        # list of years not guessed correctly
        self.year_data = years
