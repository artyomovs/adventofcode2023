from adventofcode import AdventOfCode
import re
from pprint import pprint

class Challenge(AdventOfCode):
    def parse_input(self):
        for line in self.lines:
            columns = line.split("|")
            self.parsed_input.append({
                "numbers": list(map(int, re.findall(r'\d+', columns[1]))),
                "wins": list(map(int, re.findall(r'\d+', columns[0])))[1:],
                "game": list(map(int, re.findall(r'\d+', columns[0])))[0]
            })


    def find_winnings_sum(self):

        total_sum = 0
        for line in self.parsed_input:
            count = 0
            for win in line["wins"]:
                if win in line["numbers"]:
                    count += 1
            total_sum += int(2 ** (count - 1))
        return total_sum


    def find_winnings_cards(self):
        cards = {}
        for c in self.parsed_input:
            cards[c["game"]] = 1

        for line in self.parsed_input:
            count = 0
            game = line["game"]
            for win in line["wins"]:
                if win in line["numbers"]:
                    count += 1
            for i in range(game+1, game+count+1):
                cards[i] += cards[game]
            # print(f"game = {game}. count = {count}. cards ={cards}")

        return sum(cards.values())




    def part_one(self, inputs):
        self.parse_input()
        return self.find_winnings_sum()

    def part_two(self, inputs):
        return self.find_winnings_cards()