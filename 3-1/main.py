file = open("data.txt", "r")
totals = {}
gamma = ""
epsilon = ""

for x in range(12):
    totals[x] = {"0": 0, "1": 0}

for line in file:
    binary = str(line).rstrip()
    for y in range(len(binary)):
        if (binary[y] == "1"):
            totals[y]["1"] += 1
        else:
            totals[y]["0"] += 1

for x in range(len(totals)):
    if (totals[x]["0"] > totals[x]["1"]):
        gamma += "0"
        epsilon += "1"
    else:
        gamma += "1"
        epsilon += "0"

print(int(gamma, 2) * int(epsilon, 2))


# iterate through the numbers
# total 1's and 0's for each place in the number (12 places)
# decide which has biggest total - assign to gama
# assign other to epsilon
# convert to decimal
# print out their product


# answer = "".join(map(lambda entry: str(entry), x))
