
def extrapolate(arr):
    total = 0
    for i in range(len(arr) - 2, - 1, -1):
        total = arr[i][0] - total
    return total

def next_row(arr):
    next_row = []
    zero = True
    for i in range(1, len(arr)):
        diff = arr[i] - arr[i - 1]
        next_row.append(diff)
        if diff != 0: zero = False
    return (next_row, zero)


def solve(filename:str) -> int:

    arrays = []

    with open(filename) as reader:
        for line in reader.readlines():
            arrays.append([int(i) for i in line.split()])

    total = 0

    for arr in arrays:
        curr = [arr]
        while True:
            next_, zero = next_row(curr[-1])
            curr.append(next_)
            if zero : break

        total += extrapolate(curr)
        

    return total



    

    







print(solve("/Users/zhijiazhang/Desktop/advent-of-code-2023/day9/puzzle9.txt"))