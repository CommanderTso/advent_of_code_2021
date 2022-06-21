file = open("data.txt", "r")

depth = 0
forwards = 0
aim = 0

for line in file:
    parsed = line.rstrip().split(" ")

    if (parsed[0] == "up"):
        aim -= int(parsed[1])

    if (parsed[0] == "down"):
        aim += int(parsed[1])

    if (parsed[0] == "forward"):
        forwards += int(parsed[1])
        depth += aim * int(parsed[1])


print(depth * forwards)
