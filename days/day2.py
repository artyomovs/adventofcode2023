from adventofcode import AdventOfCode
import re


COLORS = {
    "red": 12,
    "green": 13,
    "blue": 14
}

class Challenge(AdventOfCode):

    def calculate_color_sets(self):
        game_id = 0
        total_sum = 0
        color_set_multiple = 0

        for game in self.parsed_input:
            game_id += 1
            fit = True

            min_color_set = {"red": 0, "green": 0, "blue": 0}

            ## Part 1
            for cube_set in game:
                for cube in  cube_set:
                    color = cube["color"]
                    number = int(cube["number"])
                    if number > COLORS[color]:
                        fit = False
                        break
                if not(fit):
                    break
            if fit:
                total_sum += game_id

            ## Part 2
            for cube_set in game:
                for cube in  cube_set:
                    color = cube["color"]
                    number = int(cube["number"])
                    if number > min_color_set[color]:
                        min_color_set[color] = number
            color_set_multiple = color_set_multiple + min_color_set["red"] * min_color_set["green"] * min_color_set["blue"]
        return total_sum, color_set_multiple



    def parse_input(self, inputs):
        lines = [re.sub(r'^Game \d+: ', '', line) for line in inputs]

        games = []
        for line in lines:
            sets = line.strip().split(";")
            total_set = []
            for s in sets:
                color_numbers = s.split(",")
                color_sets = []
                for c in color_numbers:
                    color = c.strip(" ").split(" ")[1]
                    number = c.strip(" ").split(" ")[0]
                    color_sets.append({"color": color, "number": number})
                total_set.append(color_sets)
            games.append(total_set)

        self.parsed_input = games



    def part_one(self, inputs):
        self.parse_input(inputs)
        return self.calculate_color_sets()[0]

    def part_two(self, inputs):
        self.parse_input(inputs)
        return self.calculate_color_sets()[1]