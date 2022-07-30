# import classes from other .py files here
from game.parachute import Parachute
from game.word import Word
import time


class Director:

    """A person who directs the game. 

    The responsibility of a Director is to control the sequence of play.

    Attributes:
        is_playing (boolean): Whether or not to keep playing.
        _parachute (Parachute): an istance of Parachute.
        _word (Word): an istance of Word.
    """

    def __init__(self):
        """Constructs a new Director.

        Args:
            self (Director): an instance of Director.
        """
        self._is_playing = True
        self._parachute = Parachute()
        self._word = Word()

    def start_game(self):
        """Starts the game by running the main game loop.

          Args:
            self (Director): an instance of Director.
        """

        # display a few start up messages
        print(f"\nWelcome to jumper!\n")
        self._word.choose_word()
        self._word.reset_revealed_list()
        self._word.display_revealed_list()
        self._parachute.display_parachute()
        # - - - - - - - - - - - - - - - -
        # *

        # main game loop runs until we lose
        while self._is_playing:
            self._get_inputs()
            self._do_updates()
            self._do_outputs()

        if self._parachute.get_ropes_left() == 0:
            # This code will run after the game loop is broken if the player lost
            # print a bunch of dots to make it seem like we are falling
            for x in range(0, 30):
                print(".")
                time.sleep(0.02)
            # Display a game-end message
            print(f"SPLAT!\n\nYou just lost the game.\n")

    def _get_inputs(self):
        """ Get the next letter the player wants to guess
        Args:
            self (Director): An instance of Director.
        """

        # fix later to validate input is single letter
        self._word.set_guessed_letter(input("guess a letter: "))

    def _do_updates(self):
        """See if the player was right or not, and update parachute and revealed letters

        Args:
            self (Director): An instance of Director.
        """

        # see if the player's guess was right
        result = self._word.try_players_guess(self._word.get_guessed_letter())

        # if the player guessed incorrectly
        if result == False:

            # remove one our parachutes
            concequence = self._parachute.remove_rope()

            # if we just remoed the last rope, concequence will return True
            if concequence:
                # Player just lost the game!

                # Setting _is_playing to False breaks the game loop
                self._is_playing = False

        if result == "YOU WON!":
            # stop game play
            self._is_playing = False
            print(f"\nThe word was: ")
            # Display the revealed list
            self._word.display_revealed_list()
            # print win message
            print(f"\n{result}\n")

        # *** SOMEONE NEEDS TO WRITE A METHOD HERE TO CHECK IF THE PLAYER HAS GUESSED ALL THE LETTERS!!!!!!!!!!!!!!!!!!!!!

    def _do_outputs(self):
        """Display the current state of the parachute and revealed letters

        Args:
            self (Director): An instance of Director.
        """
        if self._is_playing:
            # Display the revealed list
            self._word.display_revealed_list()

            # Display the current state of the parachute
            self._parachute.display_parachute()
