import collections

def solve(filename: str) -> int:
    mapping = collections.defaultdict(list)
    min_ = float("inf")

    with open(filename) as reader:
        seeds = [int(seed) for seed in reader.readline().split(": ")[1].split()]
        c = 0
        for line in reader.readlines():
            if line != "\n":
                if not line[0].isdigit():
                    c += 1
                else:
                    nums = line.split()
                    mapping[c].append([int(nums[0]), int(nums[1]), int(nums[2])])

        for seed in seeds:
            curr = seed
            for val in mapping.values():
                for dest_start, source_start, range in val:
                    if source_start <= curr <= source_start + range:
                        curr = dest_start + (curr - source_start)
                        break

            min_ = min(curr, min_)

    print(mapping)
    return min_


print(solve("/Users/zhijiazhang/Desktop/advent-of-code-2023/day5/puzzle5.txt"))