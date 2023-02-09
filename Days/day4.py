def part_1(input):
    draws = input[0]

    boards = []
    temp_board = []
    for i in range(2, len(input)):
        line = input[i]
        board_row = []
        for num in line.split(" "):
            if (len(num) > 0):
                board_row.append([int(num.strip()), 0])
        if not len(board_row) < 1:
            temp_board.append(board_row)

        if (i + 1 == len(input) or len(input[i + 1]) == 0):
            boards.append(temp_board)
            temp_board = []

    return find_winner(boards, draws)


def checkwin(board, draw):
    win = False
    unchecked_sum = 0
    for col in range(len(board)):
        col_sum = 0
        for row in range(len(board)):
            col_sum += board[row][col][1]
        if (col_sum == 5):
            win = True

    for row in range(len(board)):
        row_sum = 0
        for col in range(len(board)):
            is_checked = board[row][col][1]
            row_sum += is_checked
            if not is_checked > 0:
                unchecked_sum += board[row][col][0]
        if (row_sum == 5):
            win = True
    if (win):
        return unchecked_sum * draw
    else:
        return 0


def find_winner(boards, draws):
    all_winner = []
    winner_boards = []
    for d, draw in enumerate([int(d) for d in draws.split(",")]):
        # print(draw)
        for b, board in enumerate(boards):
            for board_row in board:
                for i, field in enumerate(board_row):
                    field_val = field[0]
                    if field_val == draw:
                        field[1] = 1
            if b not in winner_boards:
                win = checkwin(board, draw)
                if win > 0:
                    winner_boards.append(b)
                    all_winner.append([b, d, win])

    return all_winner[-1][2]


def run():
    file = open('../Inputs/day4.txt')
    input = file.read().split('\n')
    count = part_1(input)
    # count = part_2(input)

    print(f'{count}')


if __name__ == '__main__':
    run()
