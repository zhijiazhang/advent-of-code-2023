def solve(filename: str) -> int:
    total = 0
    with open(filename) as reader:

        for line in reader.readlines():
            nums = line.split(": ")[1]
            winning_nums, my_nums = nums.split(" | ")
            winning_nums = set([num for num in winning_nums.split()])
            my_nums = [num for num in my_nums.split()]

            line_total = 0

            for num in my_nums:
                if num in winning_nums:
                    if line_total == 0:
                        line_total += 1
                    else:
                        line_total *= 2

            total += line_total

    return total