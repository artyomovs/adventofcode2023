from adventofcode import AdventOfCode
import re

class Challenge(AdventOfCode):

    def parse_input(self):
        self.parsed_input = [(int(t), int(d)) for t, d in zip(re.findall(r'\d+', self.lines[0]), re.findall(r'\d+', self.lines[1]))]

    def find_best_time_options(self, value) -> int:
        total_time, distance = value
        good_results_count = 0
        for i in range(1, total_time):
            new_distance = (total_time - i) * i
            if new_distance > distance:
                good_results_count += 1
        return good_results_count

    def part_one(self, inputs):
        self.parse_input()
        good_results_multi = 1
        for value in self.parsed_input:
            good_results_multi *= self.find_best_time_options(value)
        return good_results_multi

    def part_two(self, inputs):
        combined_time = int("".join(str(t[0]) for t in self.parsed_input))
        combined_distance = int("".join(str(t[1]) for t in self.parsed_input))
        return self.find_best_time_options([combined_time, combined_distance])
