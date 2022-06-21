file = open("data.txt", "r")

counter = 0
last_number = -1

for number in file:
    number = int(number)

    if (last_number == -1):
        last_number = number
        print(f"Last was -1, so new is {last_number}")
        continue

    if (number > last_number):
        counter += 1
        print(
            f"Last was {last_number}, new was {number}, incrementing counter to {counter}")
        last_number = number
    else:
        print(
            f"Last was {last_number}, new was {number}, leaving counter at {counter}")
        last_number = number

print(counter)
