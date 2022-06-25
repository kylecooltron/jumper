
from game.display_jumper_image import display_jumper_image
from game.get_random_word import get_random_word
from game.play_Jumper_game import play_Jumper_Game
from game.read_Jumper_words import read_Jumper_words


class Director:

    def __init__(self):
        game_play = ""
        Jumper_word_list = []
        dictionary_word_list = []
        random_word = ""
        jumper_word = ""

    def start_game(self):
        print("Welcome to Jumper Game")
        input("Press enter to start...")
        dictionary_word_list = read_Jumper_words.read_Jumper_words("jumper.csv", 0)
        self.random_word_nc = get_random_word.get_random_word(dictionary_word_list)
        self.random_word = self.random_word_nc.upper()
        self.jumper_word = ["#" for i in range(len(self.random_word))]
        new_record_guesses = play_Jumper_Game.play_Jumper_Game(self.random_word, 0, 0, "", self.jumper_word, 0, 5, "", "")