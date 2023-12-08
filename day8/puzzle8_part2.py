import collections
import math

def calc(format, map_, start):
    curr, moves = start, 0
    while True:    
        for move in format:
            if curr[2] == "Z": return moves
            if move == "R": curr = map_[curr][1]
            else: curr = map_[curr][0]
            moves += 1

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

    starts = [k for k in map_.keys() if k[2] == "A" ]
    return math.lcm(*[calc(format, map_, s)  for s in starts])

