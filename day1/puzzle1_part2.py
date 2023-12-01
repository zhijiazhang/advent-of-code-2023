nums = {
    "o" : [("1", "one", 3)],
    "t" : [("2", "two", 3), ("3", "three", 5)],
    "f" : [("4", "four", 4), ("5", "five", 4)],
    "s" : [("6", "six", 3), ("7", "seven", 5)],
    "e" : [("8", "eight", 5)],
    "n" : [("9", "nine", 4)]
}

def calc(line: str, i: int, n: int) -> str:
    char = line[i]
    if char.isnumeric(): return char
    if char not in nums: return None
    
    for digit, number, length in nums[char]:
        if i + length - 1 < n and line[i:i+length] == number:
                return digit
        

def left_digit(line: str, n: int) -> str:
    for i in range(n):
        res = calc(line, i, n)
        if res: return res

def right_digit(line:str, n: int) -> str:
    for i in range(len(line) - 1, - 1, -1):
        res = calc(line, i, n)
        if res: return res


def solve(filename: str) -> int:
    total = 0

    with open(filename, "r") as reader:
        for line in reader.readlines():
            n = len(line)
            total += int(left_digit(line, n) + right_digit(line, n))
                     
    return total


