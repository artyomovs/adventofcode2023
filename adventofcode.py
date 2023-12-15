from pathlib import Path

class AdventOfCode:
    def __init__(self, sample: bool = False):
        self.lines = Path("input.txt").read_text().splitlines()
        self.sample_lines = Path("sample_input.txt").read_text().splitlines()
        self.sample = sample
        self.result = "PLACEHOLDER"
        self.parsed_input = []

    def solve_quest(self):
        lines = self.sample_lines if self.sample else self.lines
        part_one = self.part_one(lines)
        part_two = self.part_two(lines)

        return part_one, part_two
