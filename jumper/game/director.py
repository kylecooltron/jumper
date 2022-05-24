# import classes from other .py files here
from game.parachute import Parachute


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
        self._parachute = Parachute()

    def start_game(self):
        """Starts the game by running the main game loop.

          Args:
            self (Director): an instance of Director.
        """

        while self._is_playing:
            self._get_inputs()
            self._do_updates()
            self._do_outputs()

    def _get_inputs(self):
        """ Get the next letter the player wants to guess

        Args:
            self (Director): An instance of Director.
        """
        print()

    def _do_updates(self):
        """See if the player was right or not, and update parachute and revealed letters

        Args:
            self (Director): An instance of Director.
        """
        print()

    def _do_outputs(self):
        """Display the current state of the parachute and revealed letters

        Args:
            self (Director): An instance of Director.
        """

        # call parachutes display method
        self._parachute.display_parachute()
