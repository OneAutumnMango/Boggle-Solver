import random

LETTER_WEIGHTS = {
    'e': 12.7, 't': 9.1, 'a': 8.2, 'o': 7.5, 'i': 7.0, 'n': 6.7, 's': 6.3,
    'h': 6.1, 'r': 6.0, 'd': 4.3, 'l': 4.0, 'c': 2.8, 'u': 2.8, 'm': 2.4,
    'w': 2.4, 'f': 2.2, 'g': 2.0, 'y': 2.0, 'p': 1.9, 'b': 1.5, 'v': 1.0,
    'k': 0.8, 'j': 0.15, 'x': 0.15, 'q': 0.1, 'z': 0.07
}
LETTERS, WEIGHTS = zip(*LETTER_WEIGHTS.items())

class Boggle:
    def __init__(self, board=None, size=4):
        self.size = size
        self.board = board or self.scramble()

    def scramble(self):
        # TODO use the dice
        self.board = [
            random.choices(LETTERS, weights=WEIGHTS, k=self.size)
            for _ in range(self.size)
        ]
        return self.board
    
    def get(self, x, y):
        if 0 <= x < self.size and 0 <= y < self.size:
            return self.board[y][x]
        raise IndexError("Out of bounds")
    
    def __getitem__(self, key):
        if isinstance(key, tuple) and len(key) == 2:
            x, y = key
            return self.get(x, y)
        raise TypeError("Use boggle[x, y] for indexing")
    
    def neighbours(self, x, y):
        offsets = [(-1, -1), (0, -1), (1, -1),
                   (-1,  0),          (1,  0),
                   (-1,  1), (0,  1), (1,  1)]
        for dx, dy in offsets:
            nx, ny = x + dx, y + dy
            if 0 <= nx < self.size and 0 <= ny < self.size:
                yield nx, ny

    def __str__(self):
        return '\n'.join(' '.join(row) for row in self.board)


if __name__ == "__main__":
    boggle = Boggle()
    print(boggle)

    print(boggle[1,1])

    print("Neighbours:")
    for nx, ny in boggle.neighbours(1, 1):
        print(f"({nx}, {ny}) = {boggle[nx, ny]}")