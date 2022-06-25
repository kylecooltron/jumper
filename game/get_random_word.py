import random

class get_random_word():
    def get_random_word(dictionary_word_list, top_score_id=1, top_name_id=2):
        random_line = random.choice(list(dictionary_word_list.values()))
        random_word = random_line[0]
        return random_word