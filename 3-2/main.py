from copy import copy

with open("data.txt", "r") as file:
    oxy_starter = [line.rstrip() for line in file]
    co2_starter = copy(oxy_starter)

    def compare(starter, keep_larger=True):
        index = 0

        while len(starter) > 1:
            zeroes = []
            ones = []

            for number in starter:
                if number[index] == "0":
                    zeroes.append(number)
                else:
                    ones.append(number)

            if keep_larger:
                starter = ones if len(ones) >= len(zeroes) else zeroes
            else:
                starter = zeroes if len(zeroes) <= len(ones) else ones

            index += 1

        return int(starter[0], 2)

    print(compare(oxy_starter))
    print(compare(co2_starter, False))
    print(compare(oxy_starter) * compare(co2_starter, False))
