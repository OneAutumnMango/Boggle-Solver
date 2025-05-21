import argparse
from utils.boggle import Boggle
from utils.boggle_solver import BoggleSolver
from utils.dictionary import DictionaryBuilder

def main():
    parser = argparse.ArgumentParser(description="Solve a Boggle board.")
    parser.add_argument("board", type=str, help="Required custom board string (e.g. 'abcdefghijklmnop')")
    args = parser.parse_args()

    board = args.board.lower()
   
    dictionary = DictionaryBuilder().get_or_build()
    # solver = BoggleSolver(dictionary, boggle)
    solver = BoggleSolver.from_string(dictionary, board)
    # print("BOARD:")
    # print(boggle)

    words = solver.solve()
    print("\nALPHABETICAL ORDER")
    print(words)

    print("\nBY LENGTH")
    print(sorted(words, key=len, reverse=True))

    print(f"Found {len(words)} words")



if __name__ == "__main__":
    main()
