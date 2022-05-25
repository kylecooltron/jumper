import random

# Parachute Class
# Author: Kyle Coulon


class Parachute:
    """The parachute

    The responsibility of parachute is to keep track of how many times the player has guessed wrong.

    Attributes:
        _TOTAL_ROPES (int): The starting number of ropes
        _ropes_left (int): Tracks how many ropes are left that the player hasn't lost by guessing wrong
        _ropes (List[string]): An array of characters that make up the lines of a parachute
        _distance (List[int]): The distance from the seeker.
    """

    def __init__(self):
        """Constructs a new Parachute.

        Args:
            self (Parachute): An instance of Parachute.
        """
        self._TOTAL_ROPES = 12
        self._ropes_left = self._TOTAL_ROPES
        self._ropes = ["_", "_", "_", "/", "_",
                       "_", "_", "\\", "\\", "/", "\\", "/"]
        self._ropes_display = []

    def display_parachute(self):
        """Constructs and prints a string that is a visual representation of the parachutes current state

        Args:
            self (Parachute): An instance of Parachute.

        Returns:
            nothing
        """

        # update _ropes_display array
        self._ropes_display = [
            " ", " ", self._ropes[0], self._ropes[1], self._ropes[2], "\n",
            " ", self._ropes[3], self._ropes[4], self._ropes[5], self._ropes[6],
            self._ropes[7], "\n", " ", self._ropes[8], " ", " ", " ", self._ropes[9], "\n",
            " ", " ", self._ropes[10], " ", self._ropes[11], "\n"]

        # print each value in that array
        # Loop through the array by incrementing the value of i
        for i in range(0, len(self._ropes_display)):
            print(self._ropes_display[i], end='')

    def remove_rope(self):
        """Removes one of the parachute ropes

        Args:
            self (Parachute): An instance of Parachute.

        Returns:
            True if the last rope was removed
            False if there are still some left
        """
        # if we have ropes left
        if self._ropes_left > 0:

            # subtract one from our counter variable
            self._ropes_left -= 1

            # turn one of the symbols in our array into a blank space
            while True:
                # choose a random value in the array
                try_rope = random.randint(0, self._TOTAL_ROPES-1)
                # see if that rope is already blank
                if self._ropes[try_rope] != " ":
                    # if not set it to a blank space
                    self._ropes[try_rope] = " "
                    # break the loop
                    break

        # if we just removed the last rope
        if self._ropes_left <= 0:
            # let the director know
            return True
        else:
            # return false
            return False
