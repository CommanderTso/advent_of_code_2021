file = open("data.txt", "r")

last_number = -1

numbers = [int(x) for x in file]
counter = 0

for index in range(2, len(numbers)):
    number = numbers[index - 2] + numbers[index - 1] + numbers[index]

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
