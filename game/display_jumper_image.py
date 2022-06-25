class display_jumper_image:
    def player_guess(guess=1):
        if guess == 2:
            print(" ")
            print(" /___\\")
            print(" \   / ")
            print("  \ / ")
            print("   O   ")
            print("  /|\\ ")
            print("  / \ ")
            print(" ")
            print("^^^^^^^")
        elif guess == 3:
            print(" ")
            print(" \   / ")
            print("  \ / ")
            print("   O   ")
            print("  /|\\ ")
            print("  / \ ")
            print(" ")
            print("^^^^^^^")
        elif guess == 4:
            print(" ")
            print(" ")
            print(" ")
            print(" ")
            print("  \ / ")
            print("   O   ")
            print("  /|\\ ")
            print("  / \ ")
            print(" ")
            print("^^^^^^^")
        elif guess == 5:
            print(" ")
            print("   x   ")
            print("  /|\\ ")
            print("  / \ ")
            print(" ")
            print("^^^^^^^")
        else:
            print(" ")
            print("  ___")
            print(" /___\\")
            print(" \   / ")
            print("  \ / ")
            print("   O   ")
            print("  /|\\ ")
            print("  / \ ")
            print(" ")
            print("^^^^^^^")

    def play_screen_update(random_word, incorrect_guesses, hidden_word, eval_guess=0, LIMIT=5, game_status="2", last_tried=""):
        print(chr(27) + "[2J")
        display_jumper_image.player_guess(len(incorrect_guesses))

        if game_status == 0:
            print(f"Game Over - the word was: {random_word} \n")
            print(f"Incorrect guesses: {incorrect_guesses} \n")
        elif game_status == 1:
            print(f"WOOOOOHOOOOOOOO \n")
            print(f"YOU WIN - the word was: {random_word} \n")
            print(f"Incorrect guesses: {incorrect_guesses} \n")
        else:
            print(f"\nHidden word: {hidden_word}")
            if len(incorrect_guesses) > 0 or len(incorrect_guesses) > 1:
                print(f"Incorrect guesses: '{incorrect_guesses}'")

            guesses_left = 0
            guesses_left = 5 - int(len(incorrect_guesses))
            print(f"{guesses_left} remaining guesses \n")