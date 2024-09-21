CardGameSimulator
Overview

CardGameSimulator is a Python-based card game that simulates a two-player competition where players draw cards from a shuffled deck. Each card has a point value, and players accumulate points until one wins by reaching or staying under a score of 21. The game dynamically compares scores and declares the winner or if both players bust.
Features

    Shuffles a full deck of 52 playing cards (Spades, Hearts, Clubs, Diamonds).
    Players draw cards and accumulate points.
    Automatic handling of Ace values (1 or 11, depending on the player’s score).
    Tracks and displays scores for each player.
    Determines the winner or if both players bust when the deck runs out or a player wins.

Prerequisites

You need the following installed on your system to run this game:

    Python 3.x

Installation

    Clone the repository to your local machine:

    bash

git clone https://github.com/your-username/CardGameSimulator.git

Navigate to the project directory:

bash

    cd CardGameSimulator

Usage

    Run the Python script to start the game:

    bash

    python CardGameSimulator.py

    The program will shuffle the deck and simulate rounds where Player 1 and Player 2 draw cards. The program will display their cards, update scores, and declare the result based on the following rules:
        A score of 21 is a win.
        If both players score 21 in the same round, it's a tie.
        If one player scores over 21, they bust, and the other player wins.
        If both players bust, it's a loss for both.

Example Output

text

Player 1 draws: Ace of Spades (Value: 1)
Player 2 draws: King of Hearts (Value: 10)
Player 1 score: 11
Player 2 score: 10

Player 1 draws: 9 of Diamonds (Value: 9)
Player 2 draws: 7 of Clubs (Value: 7)
Player 1 score: 20
Player 2 score: 17

Player 1 wins with a score of 20!

How it Works

    Deck Creation: The deck is represented as a dictionary where each card name is associated with a point value.
    Shuffling: A random shuffle function mixes up the deck.
    Game Play: The game proceeds with both players drawing cards and updating their scores. The Ace card’s value can switch from 1 to 11 based on the player’s score, ensuring maximum flexibility.

Future Enhancements

    Add graphical user interface (GUI) support.
    Implement more game variants (e.g., Blackjack rules).
    Add multiplayer support for more than two players.
