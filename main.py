import random

# List of words for the game
WORDS_LIST = ['asal', 'amir', 'hashem', 'sogol', 'sosan', 'hossein', 'emad', 'liyla', 'arash', 'amirmohamad']

def select_ai():
    """
    Selects a random word from the word list.
    :return: A randomly selected word (string).
    """
    return random.choice(WORDS_LIST)

def input_user():
    """
    Prompts the user to input a valid word from the word list.
    Ensures that the input is valid.
    :return: The user-entered word (string).
    """
    while True:
        user_input = input("Please enter a word from the list (asal, amir, hashem, sogol, sosan, hossein, emad, liyla, arash, amirmohamad): ").strip()
        if user_input in WORDS_LIST:
            return user_input
        else:
            print("Invalid input. Please try again.")

def check_guesses():
    """
    Handles the main logic of the game.
    The user has 5 attempts to guess the word selected by the AI.
    Provides feedback after each guess and displays the correct word if the user fails.
    """
    ai_word = select_ai()  # AI selects a word
    attempts = 5  # Number of allowed attempts
    print("Game started! You have 5 attempts to guess the correct word.")

    for attempt in range(attempts):
        user_word = input_user()  # Get user input
        if user_word == ai_word:
            print(f"Congratulations! You guessed the word correctly: {ai_word}")
            return
        else:
            print(f"Incorrect! You have {attempts - attempt - 1} attempts left.")

    # If the user fails to guess the word in 5 attempts
    print(f"You lost! The correct word was: {ai_word}")

if __name__ == "__main__":
    check_guesses()
