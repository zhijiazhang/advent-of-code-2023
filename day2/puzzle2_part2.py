def solve(filename: str) -> int:
    total = 0
    with open(filename, "r") as reader:
        for line in reader.readlines():
            min_colors = {
            "red" : float("-inf"), 
            "green" : float("-inf"), 
            "blue" : float("-inf")
             }
            _, games = line.split(": ")
            pairs = [pair.split() for subset in games.split(";") for pair in subset.strip().split(",")]
            for num, color in pairs: min_colors[color] = max(min_colors[color], int(num))
            
            product = 1
            for k in min_colors.keys():
                if min_colors[k] != float("-inf"):product *= min_colors[k]
            total += product

    return total