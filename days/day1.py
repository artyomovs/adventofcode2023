from adventofcode import AdventOfCode

NUMBERS = {
    "one": 1,
    "two": 2,
    "three": 3,
    "four": 4,
    "five": 5,
    "six": 6,
    "seven": 7,
    "eight": 8,
    "nine": 9,
    "ten": 10}

class Challenge(AdventOfCode):

    def get_digit_from_substr(self, substr):
        for key in NUMBERS.keys():
            if key in substr:
                return NUMBERS[key]
        return False

    def get_numbers_from_line(self, line, spell_numbers = False):
        tmp_line = ""
        for i in line:
            if spell_numbers:
                tmp_line = tmp_line + i
                result = self.get_digit_from_substr(substr=tmp_line)
                if result:
                    num = result * 10
                    break
            if i.isnumeric():
                num = int(i) * 10
                break
        tmp_line = ""
        for i in reversed(line):
            if spell_numbers:
                tmp_line = i + tmp_line
                result = self.get_digit_from_substr(substr=tmp_line)
                if result:
                    num = num + result
                    break
            if i.isnumeric():
                num += int(i)
                break
        return num

    def part_one(self, inputs):
        sum = 0
        for line in inputs:
            sum = sum + self.get_numbers_from_line(line=line)
        return sum

    def part_two(self, lines):
        sum = 0
        for line in lines:
            digits = self.get_numbers_from_line(line=line, spell_numbers=True)
            sum += digits
            # print(f"{line}. digits = {digits}. sum = {sum}")
        return sum
