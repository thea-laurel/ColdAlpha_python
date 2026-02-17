import random

def hangman():
    words = ["apple", "grapes", "mango", "banana", "orange"]
    
    chosen_word = random.choice(words)
    attempts = 6
    guessed_letters = set()
    display = ["_"] * len(chosen_word)

    print("Welcome to Hangman Game!")
    print("You have 6 incorrect guesses.\n")

    while attempts > 0 and "_" in display:
        print("Word:", " ".join(display))
        print("Attempts left:", attempts)

        guess = input("Enter a single letter: ").lower().strip()

        if not guess.isalpha() or len(guess) != 1:
            print("Please enter exactly one alphabet letter.\n")
            continue

        if guess in guessed_letters:
            print("You already tried that letter.\n")
            continue

        guessed_letters.add(guess)

        if guess in chosen_word:
            for i, ch in enumerate(chosen_word):
                if ch == guess:
                    display[i] = guess
            print("Correct!\n")
        else:
            attempts -= 1
            print("Wrong guess.\n")

    if "_" not in display:
        print("You won! The word was:", chosen_word)
    else:
        print("Game Over! The word was:", chosen_word)


if __name__ == "__main__":
    hangman()