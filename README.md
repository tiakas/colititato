# Colititato

This is a simple command-line interface (CLI) implementation of the popular Tic Tac Toe game in Python. It allows a player to play the game with a computer player by taking turns to mark the spaces on a 3x3 grid.

## Installation
To install the game, you can use pip to download and install it from PyPI:

```
pip install colititato
```

## Usage

After installation, you can start the game by running the following command in your terminal:

```
colititato
````

This will start a new game and prompt the first player to make a move. The game board will be displayed in the console as follows:

|   |   |   |
|:---:|:---:|:---:|
| 1 |  2 | 3 |
| 4 |  5 | 6 |
| 7 |  8 | 9 |

To make a move, enter the number corresponding to the cell you want to mark (1-9) and press Enter. The cell will be marked with either "X" or "O", depending on whose turn it is. The game will continue until one of the players wins, or the game ends in a tie.


## Development

To develop Colinote, first clone the repository:
```
git clone https://github.com/tiakas/colititato.git`
cd colinote
```
Then, install the development dependencies:

```
pip install -r requirements.txt
```

To run the tests, use:
```
pytest
```

To build the package, use:
```
python setup.py sdist bdist_wheel
```

This will create a dist directory containing the source distribution (*.tar.gz) and wheel distribution (*.whl) of the package.


## License

This project is licensed under the MIT License - see the LICENSE file for details.

## Contributing
Contributions are always welcome! Here are some ways to contribute:

- Fork the repository and make changes on your local branch.
- Create a pull request with your changes.
- Work on open issues.
