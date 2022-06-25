from game.display_jumper_image import display_jumper_image

class play_Jumper_Game:
    def __init__(self):
        incorrect_guesses = []
        check_guess = True

    def play_Jumper_Game(random_word, fastest_time, name_top_score, incorrect_guesses, jumper_word, eval_guess=0, num_chances=5, game_status="2", last_tried=""):
        incorrect_guesses = []
        check_guess = True
        while check_guess:
            # print(random_word)
            if len(incorrect_guesses) == num_chances:
                display_jumper_image.play_screen_update(
                    random_word, incorrect_guesses, jumper_word, game_status=0)
                return 5
            if "#" not in jumper_word:
                display_jumper_image.play_screen_update(
                    random_word, incorrect_guesses, jumper_word, game_status=1)
                return len(incorrect_guesses)
            display_jumper_image.play_screen_update(random_word, incorrect_guesses, jumper_word,
                                                    eval_guess, num_chances, game_status, last_tried)
            letter_guess = input(
                "Please select a letter or type quit: ").upper()
            if letter_guess.lower() == "quit":
                print("We are sad to see you leave.")
                return "quit"
            if letter_guess.isalpha() and len(letter_guess) == 1:
                if letter_guess in incorrect_guesses or letter_guess in jumper_word:
                    eval_guess = 4
                    print()
                    print("You have already tried this letter, try again")
                    letter_guess = input("Press the enter key to continue    ")
                elif letter_guess in random_word:
                    last_tried = letter_guess
                    eval_guess = 1
                    for i in range(len(random_word)):
                        if letter_guess == random_word[i]:
                            jumper_word[i] = letter_guess
                elif letter_guess not in incorrect_guesses:
                    game_status = 2
                    incorrect_guesses.append(letter_guess)
                    last_tried = letter_guess
            else:
                eval_guess = 3
                print()
                print("You have made an invalid choice , try again")
                letter_guess = input("Press the enter key to continue    ")