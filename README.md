# Boggle Solver

This is a **Boggle solver** implemented in Python. It uses a **dictionary tree (trie)** data structure for efficient word and prefix checking, combined with a **Depth-First Search (DFS)** algorithm to explore possible words on the Boggle board.

---

## Features

- **Dictionary Tree (Trie)**  
  Efficiently stores a large dictionary of words, allowing quick lookups to check if a current letter sequence is a valid prefix or complete word. This enables early pruning during the search.

- **Depth-First Search (DFS)**  
  Recursively explores the Boggle board starting from each letter, building words by moving to adjacent letters (including diagonals), while avoiding revisiting the same cell in the current path.

- **Customizable Board Size**  
  Supports different board sizes, although standard Boggle is 4x4.

---

## How It Works

1. **Load Dictionary into Trie**  
   The dictionary file is parsed, and each word is inserted into the tree where each node represents a letter.

2. **Generate or Load Boggle Board**  
   The board is a grid of letters. It can be randomly generated or manually specified.

3. **Search for Words**  
   Starting from each cell on the board, the solver performs a DFS, following adjacent cells to form letter sequences. At each step, it checks the trie to verify if the current sequence is a valid prefix. If not, it backtracks early.

4. **Collect Valid Words**  
   Whenever a complete word from the dictionary is formed, it is added to the list of found words.

---

## Usage

```python
from tree import Tree
from boggle import Boggle
from boggle_solver import BoggleSolver

# Load dictionary tree
dictionary = DictionaryBuilder().get_or_build()

# Create a Boggle board (random or fixed)
board = Boggle()

# Initialize solver
solver = BoggleSolver(dictionary, board)

# Solve and print set of found words
words = solver.solve()
print(words)
