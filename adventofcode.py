from pathlib import Path

class AdventOfCode:
    def __init__(self, day: int = 1, sample: bool = False):
        self.input = Path(f"inputs/input_{day}.txt").read_text().splitlines()
        self.sample_input = Path(f"inputs/sample_input_{day}.txt").read_text().splitlines()
        self.sample = sample
        self.result = "PLACEHOLDER"
        self.parsed_input = []
        self.found_dict = {}
        self.lines = []

    def solve_quest(self):
        self.lines = self.sample_input if self.sample else self.input
        lines = self.lines
        part_one = self.part_one(lines)
        part_two = self.part_two(lines)

        return part_one, part_two
