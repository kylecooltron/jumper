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

        # This code will run once at the start of the game
        # You can call a function here from the Word class that chooses a random word from a list
        # then either a new or that same method in Word class needs to break the word down into into a list of letters
        # and store it in the _letters_list attribute

        # then simply uncomment the following code: (and remove Kyle's test code)
        #
        # # create a list of underscores "_" that is the same size
        # self._word.reset_revealed_list()
        # # display that starting list to the player
        # self._word.display_revealed_list()
        # # display the starting parachute for the first time
        # self._parachute.display_parachute()
        #
        #

        # *
        # * * * Kyle's test code - - - - - - - - RAMOVE LATER
        # manually setting up a word
        self._word.set_letters_list(["T", "E", "S", "T"])
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

        # This code will run after the game loop is broken: (Kyle's code)
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

        # You guys need to call a method of the Word class HERE (or create a Guesser class) that
        # gets input from the player and makes sure it's a single letter
        # in that method you also need to make sure it has not already been revealed
        # you can call the self._word.is_letter_in_list(letter,list) which accepts any letter and list
        # if it returns true you need to tell the player something like "you've already guessed that"
        # and have them try again
        # (if you do use a Guesser class, make sure it communicates the letter input to the Word class using self._word._guessed_letter = whatever)

        # *
        # * * * Kyle's test code - - - - - - - - RAMOVE LATER
        # (guessed letter input should be handled in a method within the Word class)
        self._word.set_guessed_letter(input("guess a letter: "))
        # - - - - - - - - - - - - - - - -
        # *

    def _do_updates(self):
        # (Kyle wrote this method)
        """See if the player was right or not, and update parachute and revealed letters

        Args:
            self (Director): An instance of Director.
        """

        # see if the player's guess was right
        result = self._word.try_players_guess(self._word.get_guessed_letter())

        # if the player guessed incorrectly
        if not result:

            # remove one our parachutes
            concequence = self._parachute.remove_rope()

            # if we just remoed the last rope, concequence will return True
            if concequence:
                # Player just lost the game!

                # Setting _is_playing to False breaks the game loop
                self._is_playing = False

        # *** SOMEONE NEEDS TO WRITE A METHOD HERE TO CHECK IF THE PLAYER HAS GUESSED ALL THE LETTERS!!!!!!!!!!!!!!!!!!!!!

    def _do_outputs(self):
        # (Kyle wrote this method)
        """Display the current state of the parachute and revealed letters

        Args:
            self (Director): An instance of Director.
        """

        # Display the revealed list
        self._word.display_revealed_list()

        # Display the current state of the parachute
        self._parachute.display_parachute()
