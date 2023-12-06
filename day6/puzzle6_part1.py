def solve(filename:str) -> int:
    with open(filename) as reader:
        times = reader.readline().split(":")[1].strip().split()
        distance = reader.readline().split(":")[1].strip().split()

        make_history = 1

        for time, record in zip(times, distance):
            ways = 0

            for i in range(1, int(time)):
                if (int(time) - i) * i > int(record):
                    ways += 1

            if ways: make_history *= ways
    
    return make_history
