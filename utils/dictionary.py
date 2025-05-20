import pickle
from pathlib import Path
from tree import Tree

class DictionaryBuilder:
    def __init__(self):
        pass
    
    def _build(self, dict_path: Path): 
        with open(dict_path, 'r') as f:
            words = f.read().splitlines()

        tree = Tree()
        for word in words:
            tree.insert(word)
        return tree
    
    def get_or_build(self, dict_path: Path, rebuild=False):
        pkl_path = Path("tree.pkl")
        if rebuild or not pkl_path.exists():
            tree = self._build(dict_path)
            with open(pkl_path, 'wb') as f:
                pickle.dump(tree, f)
        else:
            with open(pkl_path, 'rb') as f:
                tree = pickle.load(f)
        return tree
        
        

if __name__ == "__main__":
    builder = DictionaryBuilder()
    dict_path = Path("words_alpha.txt")
    tree = builder.get_or_build(dict_path)

    print(tree.is_word("cat"))