def solve(filename: str) -> int:

    card_count = {}

    with open(filename) as reader:
        for line in reader.readlines():
            card, nums = line.split(": ")
            cardId = int(card.split()[1])
            winning_nums, my_nums = nums.split(" | ")
            winning_nums = set([num for num in winning_nums.split()])
            my_nums = [num for num in my_nums.split()]

            line_total = 0

            for num in my_nums:
                if num in winning_nums:
                    line_total += 1
                        
            card_count[cardId] = card_count.get(cardId, 0) + 1

            while line_total > 0:
                next_id = cardId + line_total
                if next_id <= 214:
                    card_count[next_id] = card_count.get(next_id, 0) + card_count.get(cardId)
                line_total -= 1 

    return sum(card_count.values())