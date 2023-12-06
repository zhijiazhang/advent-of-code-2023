import collections

def merge_intervals(intervals):
    if not intervals: return []
    intervals.sort(key=lambda i:i[0])
    merged = []

    for start, end in intervals:
        if not merged:
            merged.append([start, end])
        else:
            if start >= merged[-1][0] and start <= merged[-1][1]:
                if end > merged[-1][1]:
                    merged[-1][1] = end
            else:
                merged.append([start, end])
    return merged


def push(input_intervals, current_mappings):
    intervals = [] #result of all intervals split
    
    for s_start, s_end in input_intervals:
        overlap = []
        not_overlap = []
        offset_map = {}

        for offset, m_start, m_end in current_mappings:

            if m_start <= s_start <= m_end or m_start <= s_end <= m_end or s_start <= m_start <= m_end <= s_end:
                new_interval = (max(s_start, m_start), min(s_end, m_end))
                overlap.append([new_interval[0], new_interval[1]])
                offset_map[new_interval] = offset

        if not overlap:
            intervals.append([s_start, s_end])

        else:
            overlap.sort(key = lambda i:i[0])
            if overlap[0][0] > s_start:
                not_overlap.append([s_start, overlap[0][0] - 1])  

            if overlap[-1][1] < s_end:
                not_overlap.append([overlap[-1][1] + 1, s_end])

            for i in range(len(overlap) - 1):
                if abs(overlap[i][1]  - overlap[i + 1][0]) > 1:
                    not_overlap.append([overlap[i][1] + 1, overlap[i + 1][0] - 1])

            for i in range(len(overlap)):
                start, end = overlap[i]
                offset = offset_map[(start, end)]
                overlap[i] = [start + offset, end + offset]
                intervals.append(overlap[i])

            intervals.extend(not_overlap)

    return merge_intervals(intervals)



def solve(filename: str) -> int:
    mapping = collections.defaultdict(list)
    min_ = float("inf")

    with open(filename) as reader:
        seeds = [int(seed) for seed in reader.readline().split(": ")[1].split()]
        seeds_range = []

        for i in range(0, len(seeds) - 1, 2):
            seeds_range.append([[seeds[i], seeds[i] + seeds[i + 1] - 1]])
        c = 0
        for line in reader.readlines():
            if line != "\n":
                if not line[0].isdigit():
                    c += 1
                else:
                    nums = line.split()
                    mapping[c].append([int(nums[0]), int(nums[1]), int(nums[2])])

        mapping_adjusted = []

        for m in mapping.values():
            temp = []
            for d, s, r in m:
                temp.append([d - s, s, s + r - 1])
            mapping_adjusted.append(temp)


        for seed in seeds_range:
            curr = seed
            for m in mapping_adjusted:
                curr = push(curr, m)

            min_ = min(min_, curr[0][0])

    return min_
