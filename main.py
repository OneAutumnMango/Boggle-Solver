from utils.boggle import Boggle
from utils.boggle_solver import BoggleSolver
from utils.dictionary import DictionaryBuilder

def main():
    boggle = Boggle(size=4)
    dictionary = DictionaryBuilder().get_or_build()
    solver = BoggleSolver(dictionary, boggle)
    
    print(boggle)

    words = solver.solve()
    print("ALHPABETICAL ORDER")
    print(words)

    print("\nBY LENGTH")
    print(sorted(words, key=len, reverse=True))

    print(f"Found {len(words)} words")



if __name__ == "__main__":
    main()