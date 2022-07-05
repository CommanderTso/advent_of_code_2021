# I'm sure there are many cleaner and more elegant ways to do this!

class Board:
    def __init__(self):
        self.lines = [[], [], [], [], []]
        self.hits = [[0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [
            0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0]]
        self.won = False

    def __str__(self):
        output = "Lines:\n"
        for line in self.lines:
            output_line = ""
            for entry in line:
                output_line += entry + " "
            output += output_line.rstrip() + "\n"

        output += "\nHits\n"
        for line in self.hits:
            output_line = ""
            for entry in line:
                output_line += str(entry) + " "
            output += output_line.rstrip() + "\n"

        return output

    def check_number(self, pick):
        for x in range(len(self.lines)):
            for y in range(len(self.lines[x])):
                if self.lines[x][y] == pick:
                    self.hits[x][y] = 1
                    return self.check_card()

    def check_card(self):
        for line in self.hits:
            line_total = 0
            for score in line:
                line_total += score
            if line_total == 5:
                return True

        y0_total = 0
        y1_total = 0
        y2_total = 0
        y3_total = 0
        y4_total = 0
        for x in range(len(self.hits)):
            y0_total += self.hits[x][0]
            y1_total += self.hits[x][1]
            y2_total += self.hits[x][2]
            y3_total += self.hits[x][3]
            y4_total += self.hits[x][4]

        if y0_total == 5 or \
                y1_total == 5 or \
                y2_total == 5 or \
                y3_total == 5 or \
                y4_total == 5:
            return True

        if self.check_diagonals():
            return True

        return False

    def check_diagonals(self):
        line_total_1 = 0
        line_total_2 = 0

        for x in range(5):
            line_total_1 += self.hits[x][x]
            line_total_2 += self.hits[x][4-x]

        if line_total_1 == 5 or line_total_2 == 5:
            return True

    def calculate_score(self, number):
        unmarked_total = 0

        for x in range(len(self.hits)):
            for y in range(len(self.hits[x])):
                if self.hits[x][y] == 0:
                    unmarked_total += int(self.lines[x][y])

        return unmarked_total * int(number)


def main():
    calls = []
    board_set = []
    winner_found = False
    board_counter = 0

    with open("data.txt", "r") as file:
        board = Board()
        counter = 0

        for line in file:
            if len(line) > 15:
                calls = [number for number in line.rstrip().split(",")]
            elif counter == 5:
                board_set.append(board)
                board = Board()
                counter = 0
            elif line == "\n":
                pass
            else:
                board.lines[counter] = [number.lstrip()
                                        for number in line.rstrip().split()]
                counter += 1

        board_set.append(board)

    board_counter = len(board_set)
    for number in calls:
        for board in board_set:
            if board.won == False:
                print(f"Board counter: {board_counter}")
                if board.check_number(number) and winner_found == False:
                    winner_found = True
                    board.won = True
                    board_counter -= 1
                    print("First Board")
                    print(board)
                    print(board.calculate_score(number))
                elif board.check_number(number) and winner_found == True and board_counter > 1:
                    board_counter -= 1
                    board.won = True
                elif board.check_number(number) and winner_found == True and board_counter == 1:
                    print("Last Board")
                    print(board)
                    print(board.calculate_score(number))
                    return


if __name__ == '__main__':
    main()
