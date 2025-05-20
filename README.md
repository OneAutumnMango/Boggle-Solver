# Boggle Solver

This is a **Boggle solver** implemented in Python. It uses a **dictionary trie** (prefix tree) to incrementally follow valid word paths as it explores the board with **Depth-First Search (DFS)**. The solver avoids redundant work by advancing through the trie at each step, pruning invalid paths early without re-checking prefixes from the root.

---

## Requirements
- Python 3.6+ 
- A word list file (newline-delimited). You can use:
  - `sowpods.txt` from [scrabblewords/scrabblewords](https://github.com/scrabblewords/scrabblewords)
  - Or any plain text file with one word per line
---

## Usage

Run the solver from the command line:

```bash
python main.py muyvtsndlbaiewfl
```

This example provides a 4x4 Boggle board using the letters a–p. The solver prints all found words, sorted alphabetically and by length.

---

## Example Output

```
❯ python main.py muyvtsndlbaiewfl
BOARD:
m u y v
t s n d
l b a i
e w f l

ALPHABETICAL ORDER:
['abe', 'abel', 'abl', 'able', ...]

BY LENGTH:
['findable', 'finable', 'sunbelt', 'sundial', ...]
Found 308 words
```

---

## Project Structure

```
.
├── main.py               # CLI entry point
├── sowpods.txt           # Word list
├── tree.pkl              # Cached trie (auto-generated)
└── utils/
    ├── __init__.py
    ├── tree.py           # Trie implementation
    ├── dictionary.py     # Dictionary loader/builder
    ├── boggle.py         # Boggle board representation
    └── boggle_solver.py  # DFS word solver
```

---

## Customization

- Change the board size by modifying the `Boggle` class `size` argument (default is 4×4).
- Replace `sowpods.txt` with your preferred dictionary.

