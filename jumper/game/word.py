

# Word Class

class Word:
    """The word

    The responsibility of word is to randomly select a word from a list and reveal letters from that word if the player guesses them

    Attributes:
        _word_list (list[int]): a list of words 
        _word_list (list[int]): a list of words
        _word_list (list[int]): a list of words 
        _word_list (list[int]): a list of words 
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
        # I haven't used this attribute, but I'm putting it here as an example of what name you could use
        # self._word_list = ["parachute", "computer", "example"]

        self._letters_list = []
        self._revealed_list = []
        self._guessed_letter = ""

    def reset_revealed_list(self):
        """This function sets the _revealed_list to a bunch of underscore "_" characters
        the number of characters in the list is made equal to the length of the _letters_list

        Args:
            self (Parachute): An instance of Parachute.

        Returns:
            Nothing
        """
        # remove all items from the current list
        self._revealed_list.clear()

        # for every letter in _letters_list
        for i in self._letters_list:

            # create a new underscore in the _revealed_list
            self._revealed_list.append("_")

    def display_revealed_list(self):
        """Prints out the current _revealed_list

        Args:
            self (Parachute): An instance of Parachute.

        Returns:
            Nothing
        """
        # Loop through the array by incrementing the value of i
        for i in range(0, len(self._revealed_list)):
            # print each value in the list
            print(self._revealed_list[i], end='')

        # print a blank space underneath
        print()

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
        # Iterate through each letter in the letters_list and see if it matches the letter argument
        for val in letters_list:

            # if the current letter we are looping through matches
            if val.upper() == letter.upper():
                # we found the letter return True
                return True

        # if the letter was not found return false
        return False

    def reveal_correct_letters(self, guessed_letter):
        """Iterates through the _letters_list and reveal letters that match the guessed_letter
           in the corrosponding location in the _revealed_list

        Args:
            self (Parachute): An instance of Parachute.
            guessed_letter (string): A single letter the player has guessed

        Returns:
            Nothing
        """
        # Iterate through each letter in the _letters_list and reveal matching letters in _revealed_list
        for i, val in enumerate(self._letters_list):

            # if this letter in the list matches the guessed letter
            if(val.upper() == guessed_letter.upper()):

                # reveal it in the revealed list
                self._revealed_list[i] = val

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
            print("\n\n\nYou guessed correctly!\n")

            # reveal the correct letters in the _revealed_list
            self.reveal_correct_letters(guessed_letter)

            return True

        else:

            # the guess was wrong
            print("\n\n\nIncorrect.\n")
            return False
