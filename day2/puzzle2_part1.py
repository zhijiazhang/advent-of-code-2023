rules = {
    "red" : 12, 
    "green" : 13, 
    "blue" : 14
}

def solve(filename: str) -> int:
    total = 0
    with open(filename, "r") as reader:
        for line in reader.readlines():
            game_id, games = line.split(": ")
            if all(int(num) <= rules[color] for subset in games.split(";") for pair in subset.strip().split(",") for num, color in [pair.split()]):
                total += int(game_id.split()[1])
    return total





