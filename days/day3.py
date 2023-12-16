from adventofcode import AdventOfCode
import re

DIRECTIONS = [
    (-1, -1),  # Diagonal: Up-Left
    (-1, 0),  # Up
    (-1, 1),  # Diagonal: Up-Right
    (0, -1),  # Left
    (0, 1),  # Right
    (1, -1),  # Diagonal: Down-Left
    (1, 0),  # Down
    (1, 1),  # Diagonal: Down-Right
]


class Challenge(AdventOfCode):
    def find_column_indices(self, main_string, substring):
        indices = []

        for i in range(len(main_string)):
            if main_string[i : i + len(substring)] == substring:
                indices.extend(range(i, i + len(substring)))

        return indices

    def find_all_numbers(self, inputs):
        total_numbers = []
        for row, line in enumerate(inputs):
            for match in re.finditer(r"\d+", line):
                total_numbers.append(
                    {
                        "row": row,
                        "columns": list(range(match.start(), match.end())),
                        "number": match.group(),
                    }
                )
        self.parsed_input = total_numbers

    def check_adjacents(self, number, part="one"):
        row = number["row"]
        for col in number["columns"]:
            for d in DIRECTIONS:
                new_row = row + d[0]
                new_col = col + d[1]

                if (
                    new_row >= 0
                    and new_row < len(self.lines) - 1
                    and new_col >= 0
                    and new_col < len(self.lines[0])
                ):
                    symbol = self.lines[new_row][new_col]
                    if part == "one":
                        if symbol != "." and not (symbol.isnumeric()):
                            number["adj"] = True
                            return True
                    else:
                        if symbol == "*":
                            key_name = f"{new_row}_{new_col}"
                            if key_name in list(self.found_dict.keys()):
                                self.found_dict[key_name].append(number["number"])
                            else:
                                self.found_dict[key_name] = [number["number"]]
                            return True

        number["adj"] = False

    def find_all_adjacents(self, part="one"):
        for number in self.parsed_input:
            self.check_adjacents(number, part=part)

    def get_asterisks_sum(self):
        total_sum = 0
        for key, numbers in self.found_dict.items():
            if len(numbers) > 1:
                multi = 1
                for n in numbers:
                    multi *= int(n)
                total_sum += multi
        return total_sum

    def get_sum_with_adjacents(self):
        elements_with_adjacents = [number["number"] for number in self.parsed_input if number["adj"]]
        total_sum = 0

        for element in elements_with_adjacents:
            total_sum += int(element)
        return total_sum

    def part_one(self, inputs):
        self.find_all_numbers(inputs)
        self.find_all_adjacents(part="one")
        return self.get_sum_with_adjacents()

    def part_two(self, inputs):
        self.find_all_numbers(inputs)
        self.find_all_adjacents(part="two")
        return self.get_asterisks_sum()
