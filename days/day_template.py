"""Day template for Advent of Code 2025.

Copy this to `day01.py`, implement `solve_part1` and `solve_part2`, and `main()` will return both results.
"""
from pathlib import Path

INPUT_FILE = Path(__file__).with_name('input.txt')

def read_input():
    if INPUT_FILE.exists():
        return INPUT_FILE.read_text().splitlines()
    return []


def solve_part1(lines):
    # Implement part 1
    return None


def solve_part2(lines):
    # Implement part 2
    return None


def main():
    lines = read_input()
    p1 = solve_part1(lines)
    p2 = solve_part2(lines)
    return (p1, p2)


if __name__ == '__main__':
    print(main())
