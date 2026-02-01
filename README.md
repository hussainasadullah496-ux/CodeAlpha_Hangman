# Hangman Game

A classic Hangman game implemented in Python. Guess the hidden word one letter at a time before the hangman is complete!

![Hangman Logo](https://img.shields.io/badge/Game-Hangman-blue.svg)

## 🎮 Features

- **Random Word Selection**: The game picks a random word from a predefined list for every new session.
- **ASCII Art Visuals**: Dynamic ASCII art displays the hangman's progress as you make incorrect guesses.
- **Input Validation**: Ensures users enter only single alphabetic characters and prevents duplicate guesses.
- **Colorized Output**: Uses ANSI escape codes for a more vibrant terminal experience (e.g., green welcome message).
- **History Tracking**: Keeps track of all guessed letters to help you play smarter.

## 🚀 How to Run

1.  **Prerequisites**: Make sure you have Python installed on your system.
2.  **Clone/Download**: Save the `h.py` file to your local machine.
3.  **Run the script**:
    ```bash
    python h.py
    ```

## 🕹️ How to Play

1.  The computer selects a secret word.
2.  You start with 6 "lives" (incorrect guesses allowed).
3.  On each turn, enter a single letter you think might be in the word.
4.  If the letter is in the word, it will be revealed in its correct position(s).
5.  If the letter is not in the word, a part of the hangman will be drawn.
6.  **Win**: Reveal all the letters in the word before running out of guesses.
7.  **Loss**: The hangman is fully drawn after 6 incorrect guesses.

## 🛠️ Built With

- **Python**: Core logic and terminal interactions.
- **Random Module**: For word selections.

---
Enjoy the game! 🎈
