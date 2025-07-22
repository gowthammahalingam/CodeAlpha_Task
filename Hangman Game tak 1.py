import random

def hangman_game():
    print("--- Hangman Game ---")
    words = ["python", "hangman", "programming", "developer", "computer"]
    word = random.choice(words).lower() # Choose a random word and convert to lowercase
    guessed_letters = [] # To store all letters the user has guessed
    incorrect_guesses = 0
    max_incorrect_guesses = 6
    # Create the initial display word (e.g., "______" for "python")
    display_word = ["_" for _ in word]

    print("Welcome to Hangman!")
    print("Guess the word:")
    print(" ".join(display_word)) # Display the underscores/guessed letters

    # Main game loop: continues as long as guesses are left and word isn't guessed
    while incorrect_guesses < max_incorrect_guesses and "_" in display_word:
        guess = input("Guess a letter: ").lower() # Get user's guess

        # Input validation
        if len(guess) != 1 or not guess.isalpha():
            print("Invalid input. Please enter a single letter.")
            continue # Skip to the next loop iteration

        if guess in guessed_letters:
            print(f"You already guessed '{guess}'. Try again.")
            continue # Skip to the next loop iteration

        guessed_letters.append(guess) # Add the new guess to the list of guessed letters

        if guess in word:
            print(f"Good guess! '{guess}' is in the word.")
            # Update the display_word with the correctly guessed letter
            for i, char in enumerate(word):
                if char == guess:
                    display_word[i] = guess
        else:
            incorrect_guesses += 1
            print(f"Sorry, '{guess}' is not in the word. You have {max_incorrect_guesses - incorrect_guesses} incorrect guesses left.")

        print(" ".join(display_word)) # Show the current state of the word
        print(f"Guessed letters: {', '.join(sorted(guessed_letters))}") # Show all guessed letters

    # After the loop, check if the player won or lost
    if "_" not in display_word:
        print(f"\nCongratulations! You guessed the word: {word}")
    else:
        print(f"\nGame Over! You ran out of guesses. The word was: {word}")
    print("-" * 20) # Separator for output

# To run the Hangman game:
if __name__ == "__main__":
    hangman_game()