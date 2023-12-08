def solve(filename:str)-> int:
    map_ = {}
    format = ""
    
    with open(filename) as reader:
        format += reader.readline()
        format += reader.readline()
        format = format.strip("\n")
        for line in reader.readlines():
            if line == "\n": continue
            node, next_ = line.split(" = ")
            map_[node] = (next_[1:4], next_[6:9])

    curr = "AAA"
    moves = 0
    while True:
        for move in format:
            if curr == "ZZZ": return moves
            if move == "R": curr = map_[curr][1]
            else: curr = map_[curr][0]
            moves += 1