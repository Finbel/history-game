
class Screen(object):

    def __init__(self, screen_file):
        # The screen to which things are written
        self.canvas = screen_file
        players = []
        current_player = 0
        message = ""
