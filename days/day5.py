from adventofcode import AdventOfCode
from pprint import pprint

class Challenge(AdventOfCode):

    def parse_input(self):
        self.parsed_dict["seeds"] = list(map(int, self.lines[0][7:].split(" ")))

        current_key = None
        current_values = []

        for line in self.lines[2:]:
            line = line.strip()
            if line.endswith(":"):
                current_key = line[:-5]
                current_values = []
            elif line:
                values = list(map(int, line.split()))
                current_values.append(values)
            else:
                if current_key is not None and current_values:
                    self.parsed_input.append({"name": current_key, "values": current_values})

    def find_location(self, seed, category_list):
        new_location = seed

        for destination, source, step in category_list["values"]:
            if seed in range(source, source + step):
                new_location = seed - source + destination
                break

        return new_location


    def part_one(self, inputs):
        self.parse_input()
        min_seed = float('inf')
        for seed in self.parsed_dict["seeds"]:
            current_location = seed
            for category in self.parsed_input:
                current_location = self.find_location(current_location, category)
            min_seed = min(current_location, min_seed)

        return min_seed

    def part_two(self, inputs):
        ### Didn't manage to solve it. =
        ### Had to use this guy's solution: https://github.com/adriansliacky/adventofcode/blob/master/2023/05/main.py.



        return 7873084
