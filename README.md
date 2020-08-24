# Playing Card Games
A small project to apply my Python learning.

## Description
Included is a `playingcards` library with a `table` module, designed to emulate a playing card deck(s) with players sitting at a table.

The module, `from playingcards import table`, defines a `Player` class with attributes `name` (string), `dealer` (boolean, defaults to False) and `money` (integer, defaults to 100).
There's also a `Dealer` subclass of the `Player` class.

Functions defined for the playing cards include `shuffle_deck`, `deal_card` and `print_hand`.

Check out the `blackjack.py` for an example on how to use the `playingcards` library.
