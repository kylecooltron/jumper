import random


class Parachute:
    """The parachute

    The responsibility of parachute is to keep track of how many times the player has guessed wrong.

    Attributes:
        _location (int): The location of the hider (1-1000).
        _distance (List[int]): The distance from the seeker.
    """

    def __init__(self):
        """Constructs a new Parachute.

        Args:
            self (Parachute): An instance of Parachute.
        """
        self._location = random.randint(1, 1000)
        self._distance = [0, 0]  # start with two so get_hint always works

    def display_parachute(self):
        """Constructs a string that is a visual representation of the parachutes current state

        Args:
            self (Parachute): An instance of Parachute.

        Returns:
            string: returns a string 
        """
        chute_display_string = ";)"

        return chute_display_string
