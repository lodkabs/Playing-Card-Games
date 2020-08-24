# Playing Card Games
A small project to apply my Python learning.

## Description
Included is a `playingcards` library with a `table` module, designed to emulate a playing card deck(s) with players sitting at a table.

The module, `from playingcards import table`, defines a `Player` class with attributes `name` (string), `dealer` (boolean, defaults to False) and `money` (integer, defaults to 100).
There's also a `Dealer` subclass of the `Player` class.

Functions defined for the playing cards include `shuffle_deck`, `deal_card` and `print_hand`.

Check out the `blackjack.py` for an example on how to use the `playingcards` library.

## To-do list
1. Allow for multiple decks in one game.
1. Allow custom decks; whether that means having a lessened playing card deck, or a deck with not-so-typical playing cards.
1. Additional card back designs to pick from (or potentially a feature to allow a user to include their own card back design)
