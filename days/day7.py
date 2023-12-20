from adventofcode import AdventOfCode
from itertools import product

CARD_LABELS = ['2', '3', '4', '5', '6', '7', '8', '9', 'T', 'J', 'Q', 'K', 'A']

class Challenge(AdventOfCode):

    def is_hand_bigger(self, hand1, hand2, with_joker = False):
        hand1_strength = self.get_hand_strength(hand1) if not with_joker else self.get_hand_strength(self.find_best_combination_with_jokers(hand1))
        hand2_strength = self.get_hand_strength(hand2) if not with_joker else self.get_hand_strength(self.find_best_combination_with_jokers(hand2))

        card_labels = list(CARD_LABELS)
        if with_joker:
            card_labels.remove("J")
            card_labels.insert(0, "J")


        if hand1_strength > hand2_strength:
            return True
        elif hand1_strength < hand2_strength:
            return False
        else:
            for i in range(0, 5):
                index_1 = card_labels.index(hand1[i])
                index_2 = card_labels.index(hand2[i])
                if index_1 == index_2:
                    continue
                elif  index_1 > index_2:
                    return True
                else:
                    return False
            return False


    def get_hand_strength(self, hand):

        symbols_count = []

        for s in set(hand):
            symbols_count.append(hand.count(s))
        symbols_count.sort()

        if symbols_count[0] == 5:
            return 7
        elif 4 in symbols_count:
            return 6
        elif 3 in symbols_count and 2 in symbols_count:
            return 5
        elif 3 in symbols_count:
            return 4
        elif symbols_count.count(2) == 2:
            return 3
        elif symbols_count.count(2) == 1:
            return 2
        else:
            return 1

    def get_sum_of_best_combinations(self, with_joker=False):
        hand = self.lines[0].split(" ")[0].strip()
        bid = int(self.lines[0].split(" ")[1].strip())
        cards = [{"hand": hand, "bid": bid}]
        total_sum = 0

        for line in self.lines[1:]:
            hand = line.split(" ")[0].strip()
            bid = int(line.split(" ")[1].strip())
            new_card = {
                "hand": hand,
                "bid": bid
            }

            for i in range(0, len(cards)):
                hand2 = cards[i]["hand"]
                if not self.is_hand_bigger(hand, hand2, with_joker=with_joker):
                    # print(f"{hand} lower {hand2}. cards: {cards}")
                    cards.insert(i, new_card)
                    break
                if i == len(cards) - 1:
                    cards.append(new_card)
                    break

        for i in range(1, len(cards) + 1):
            hand = cards[i-1]["hand"]
            total_sum += cards[i-1]["bid"] * i

            # print(f"hand {hand} rank {i} bid {bid} sum = {total_sum}")

        return total_sum


    def generate_combinations(self, input_string, replace_symbols):
        x_indices = [i for i, char in enumerate(input_string) if char == 'J']
        replacement_combinations = product(replace_symbols, repeat=len(x_indices))
        result_combinations = []
        for replacement_combination in replacement_combinations:
            new_string = list(input_string)
            for index, replacement in zip(x_indices, replacement_combination):
                new_string[index] = str(replacement)
            result_combinations.append("".join(new_string))


        return result_combinations


    def find_best_combination_with_jokers(self, hand):
        if hand.count("J") in [0, 5]:
            return hand
        all_labels = list(CARD_LABELS)
        all_labels.remove("J")
        combinations = self.generate_combinations(hand, all_labels)
        # print(combinations)
        best_combination = combinations[0]
        print(f"for hand {hand} best combination {best_combination}")
        for combination in combinations[1:]:
            if self.is_hand_bigger(combination, best_combination):
                best_combination = combination
        return best_combination


    def part_one(self, inputs):
        return self.get_sum_of_best_combinations(with_joker=False)

    def part_two(self, inputs):
        return self.get_sum_of_best_combinations(with_joker=True)