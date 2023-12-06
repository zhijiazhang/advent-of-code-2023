def solve(filename:str) -> int:
    with open(filename) as reader:
        time = "".join(reader.readline().split(":")[1].strip().split())
        distance = "".join(reader.readline().split(":")[1].strip().split())
        make_history = 0

        for i in range(1, int(time)):
            if (int(time) - i) * i > int(distance):
                make_history += 1

    return make_history

