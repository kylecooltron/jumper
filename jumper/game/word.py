

# Word Class

class Word:
    """The word

    The responsibility of word is to randomly select a word from a list and reveal letters from that word if the player guesses them

    Attributes:
        _example (int):
    """

    def __init__(self):
        """Defines variables used to:
        Select a random word from a list
        Break that word up into an array of letters
        Create an array of blank "_" spaces the same size as the word that will reveal correctly guessed letters
        determine whether a letter the player guesses is found in the letter array

        Args:
            self (Word): An instance of Word.
        """
        self._word_list = ["parachute", "computer", "example"]
        self._letters_list = []
        self._revealed_list = []

    def is_letter_in_list(self, letter, letters_list):
        """Determines whether a certain letter appears in an list of strings
           This method is used by try_players_guess() below

        Args:
            self (Parachute): An instance of Parachute.
            letter (string): The letter to check for
            letters_list [(string)]: an list of individual letter strings

        Returns:
            True if the letter does appear in letter list
            False if it didn't
        """
        # use built in method to determine how many times the letter appears in the list
        exists_count = letters_list.count(letter)

        # if count is more than 0
        if exists_count > 0:
          # return that the letter does appear in the list
            return True
        else:
          # return that the letter does not appear in the list
            return False

    def try_players_guess(self, guessed_letter):
        """Checks if the players guessed letter is found in the letters_list
        If so, reveals each instance of that letter in the correct position on the _revealed_list
        If not, returns False

        Args:
            self (Parachute): An instance of Parachute.
            guessed_letter (string): A single letter the player has guessed

        Returns:
            True if the guess was correct
            False if it wasn't
        """

        if self.is_letter_in_list(guessed_letter, self._letters_list):

            # the guess was correct
            print("You guessed correctly! \n")

            return True

        else:

            # the guess was wrong
            print("Incorrect. \n")
            return False
