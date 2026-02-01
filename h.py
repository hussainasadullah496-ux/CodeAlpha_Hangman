# Hangman Game

# Importing random module
import random

# logo
logo =r"""
 _    _                                          
| |  | |
| |__| | __ _ _ __   __ _ _ __ ___   __ _ _ __ 
|  __  |/ _` | '_ \ / _` | '_ ` _ \ / _` | '_ \\
| |  | | (_| | | | | (_| | | | | | | (_| | | | |
|_|  |_|\__,_|_| |_|\__, |_| |_| |_|\__,_|_| |_|
                    __/ |                    
                   |___/
"""

# Settings
words = ["space", "banana", "galaxy", "grape", "astronot"]
secret_word = random.choice(words)

max_wrong = 6
wrong_guesses = 0

guessed_letters = []          # keeps guess order for display
correct_letters = set()       # letters that are in the word
wrong_letters = set()         # wrong letters (unique) -> only new wrong guesses count

# 7 stages: 0..6 (6 wrong guesses allowed)
hangman_stages = [
    """
     +---+
         |
         |
         |
        ===
    """,
    """
     +---+
     O   |
         |
         |
        ===
    """,
    """
     +---+
     O   |
     |   |
         |
        ===
    """,
    """
     +---+
     O   |
    /|   |
         |
        ===
    """,
    """
     +---+
     O   |
    /|\\  |
         |
        ===
    """,
    """
     +---+
     O   |
    /|\\  |
    /    |
        ===
    """,
    """
     +---+
     O   |
    /|\\  |
    / \\  |
        ===
    """
]

print(logo)
print("\033[92mWelcome to Hangman!\033[0m")  # Green text for welcome message
print("Guess the word one letter at a time.")
print(f"You can make {max_wrong} incorrect guesses.")

# Game Loop
while wrong_guesses < max_wrong:
    # Show hangman stage
    print(hangman_stages[wrong_guesses])

    # Show guessed letters list
    print("Guessed letters:", " ".join(guessed_letters) if guessed_letters else "(none)")

    # Display word progress
    display_word = ""
    for ch in secret_word:
        display_word += ch if ch in correct_letters else "_"
    print("Word:", display_word)

    # Win check
    if "_" not in display_word:
        print("\n🎉 You guessed the word!")
        break

    # Input validation (force single letter)
    guess = input("\nGuess ONE letter: ").lower().strip()

    if len(guess) != 1 or not guess.isalpha():
        print("Please enter exactly ONE alphabet letter.\n")
        continue

    # Already guessed?
    if guess in correct_letters or guess in wrong_letters:
        print("You already guessed that letter. Try a different one.\n")
        continue

    # Record guess for display (in order)
    guessed_letters.append(guess)

    # Check guess + count only NEW wrong guesses
    if guess in secret_word:
        correct_letters.add(guess)
        print("✅ Good guess!")
    else:
        wrong_letters.add(guess)
        wrong_guesses += 1
        print("❌ Wrong guess!")
        print("Remaining incorrect guesses:", max_wrong - wrong_guesses)

# Game Over
if wrong_guesses == max_wrong:
    print(hangman_stages[wrong_guesses])
    print("❌ Game Over!")
    print("The word was:", secret_word)