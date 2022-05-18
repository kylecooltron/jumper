#from game.hider import Hider
#from game.seeker import Seeker


class Director:

    """A person who directs the game. 

    The responsibility of a Director is to control the sequence of play.

    Attributes:
        is_playing (boolean): Whether or not to keep playing.
    """

    def __init__(self):
        """Constructs a new Director.

        Args:
            self (Director): an instance of Director.
        """
        self._is_playing = True

    def start_game(self):
        """Starts the game by running the main game loop.

          Args:
            self (Director): an instance of Director.
        """

        while self._is_playing:
          # what the crap
            print()
