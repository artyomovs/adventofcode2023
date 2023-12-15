import argparse
import importlib



def main():

    parser = argparse.ArgumentParser(description="Advent of Code 2023")
    parser.add_argument("-d", "--day", dest="day", metavar="day_number", type=int, help="Day number", required=True)
    parser.add_argument("-s", "--sample", action="store_true", dest="sample", help="Whether to use sample input")
    args = parser.parse_args()

    day_solution = importlib.import_module(f"days.day{args.day}").Challenge(args.sample)
    results = day_solution.solve_quest()


    print("\n\n-------------Advent of Code 2023------------\n\n")
    if args.sample:
        print(".............SAMPLE DATA.............\n")
    print(f"Day {args.day}. Part one: {results[0]}. Part two: {results[1]}")


if __name__ == "__main__":
    main()