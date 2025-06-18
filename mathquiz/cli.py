import argparse
from mathquiz.core import Quiz

def main():
    parser = argparse.ArgumentParser(description="Math Quiz CLI")
    parser.add_argument("--num", type=int, default=10, help="Número de questões")
    parser.add_argument("--ops", nargs="+", default=["+"], help="Operações: + - * /")
    parser.add_argument("--min", type=float, default=0)
    parser.add_argument("--max", type=float, default=10)
    parser.add_argument("--decimals", action="store_true", help="Usar decimais")
    parser.add_argument("--places", type=int, default=2, help="Casas decimais")
    args = parser.parse_args()

    quiz = Quiz(args)
    quiz.run()

if __name__ == "__main__":
    main()