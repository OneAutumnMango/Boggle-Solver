from utils.tree import Tree
from utils.boggle import Boggle
from utils.dictionary import DictionaryBuilder


class BoggleSolver:
    def __init__(self, dictionary_tree: Tree, boggle: Boggle):
        self._dictionary_tree = dictionary_tree
        self._boggle = boggle
        self._found = set()

    def _enumerate(self, position): # DFS at position of boggle going through whole board
        x, y = position

        letter = self._boggle[x, y]
        node = self._dictionary_tree.start(letter)

        if node is None:
            return
        
        self._dfs(x, y, letter, node, set())

    def _dfs(self, x, y, path, node, visited):
        visited.add((x, y))

        # print(f"checking {path}: is word? {node.is_word}")
        if node.is_word:
            self._found.add(path)

        for nx, ny in self._boggle.neighbours(x, y):
            if (nx, ny) in visited:
                continue

            next_letter = self._boggle[nx, ny]
            child = node.next(next_letter)
            if child:
                self._dfs(nx, ny, path + next_letter, child, visited.copy())

    # def _dfs(self, x, y, path, node, visited):
    #     visited.add((x, y))
    #     path.append(self._boggle[x, y])

    #     if node.is_word:
    #         self._found.add(''.join(path))

    #     for nx, ny in self._boggle.neighbors(x, y):
    #         if (nx, ny) not in visited:
    #             next_letter = self._boggle[nx, ny]
    #             child = node.children.get(next_letter)
    #             if child:
    #                 self._dfs(nx, ny, path, child, visited)

    #     path.pop()              # backtrack
    #     visited.remove((x, y))  # backtrack

    def solve(self):
        for y in range(self._boggle.size):
            for x in range(self._boggle.size):
                self._enumerate((x, y))
        return sorted(self._found)
    
    def __str__(self):
        return str(self._found)
    

if __name__ == "__main__":
    boggle = Boggle(size=4)
    dictionary = DictionaryBuilder().get_or_build()
    solver = BoggleSolver(dictionary, boggle)
    
    print(boggle)

    print(solver.solve())