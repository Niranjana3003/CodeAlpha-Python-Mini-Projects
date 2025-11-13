import random

def hangman():
    words = ["papaya", "banana", "cherry", "mango", "lemon"]
    word = random.choice(words)
    guessed_letters = []
    incorrect_guesses = 0
    max_incorrect = 6

    print("Welcome to Hangman!")
    print("Guess the word, one letter at a time.")
    print("You have 6 attempts to guesses the word.")

    # Create a display version of the word with underscores
    display_word = ["_" for _ in word]

    while incorrect_guesses < max_incorrect and "".join(display_word) != word:
        print("Word: " + " ".join(display_word))
        print(f"Incorrect guesses left: {max_incorrect - incorrect_guesses}")
        guess = input("Guess a letter: ").lower()

        if len(guess) != 1 or not guess.isalpha():
            print("Please enter a single alphabetic letter.")
            continue

        if guess in guessed_letters:
            print("You already guessed that letter. Try again.")
            continue
        
        guessed_letters.append(guess)

        if guess in word:
            # Reveal the guessed letter in the display word
            for i, letter in enumerate(word):
                if letter == guess:
                    display_word[i] = guess
            print("Good guess!")
        else:
            incorrect_guesses += 1
            print("Wrong guess!")

    if "".join(display_word) == word:
        print("Congratulations! You guessed the word:", word)
    else:
        print("Sorry, you ran out of guesses. The word was:", word)

if __name__ == "__main__":
    hangman()