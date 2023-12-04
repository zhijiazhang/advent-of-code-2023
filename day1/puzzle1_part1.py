def left_digit(line: str):
    for char in line:
        if char.isnumeric():
            return char

def right_digit(line:str):
    for i in range(len(line) - 1, - 1, -1):
        if line[i].isnumeric():
            return line[i]

def solve(filename: str) -> int:
    total = 0

    with open(filename, "r") as reader:
        for line in reader.readlines():
            total += int(left_digit(line) + right_digit(line))
                     
    return total


