import numpy as np

with open("inputs/day_04.txt") as f:
    raw_data = f.readlines()


def parse_raw_data(raw_data):
    numbers = [int(i) for i in raw_data[0].strip().split(",")]
    boards = []
    board = []
    for line in raw_data[2:]:
        line = line.strip()
        if line:
            board.append([int(i) for i in line.split()])
        else:
            boards.append(board)
            board = []

    boards.append(board)

    return numbers, np.array(boards)


numbers, boards = parse_raw_data(raw_data)
mask = np.zeros_like(boards, dtype=bool)

for num in numbers:
    mask[np.where(boards == num)] = True
    check_col = np.all(mask, axis=1)
    check_row = np.all(mask, axis=2)
    if np.any(check_col) or np.any(check_row):
        break

if check_col.sum():
    board_to_check = check_col
else:
    board_to_check = check_row
board_index = np.where(board_to_check == 1)[0][0]

print("sol_a", boards[board_index][~mask[board_index]].sum() * num)

numbers, boards = parse_raw_data(raw_data)
mask = np.zeros_like(boards, dtype=bool)

scores = []

for num in numbers:
    mask[np.where(boards == num)] = True
    check_col = np.all(mask, axis=1)
    check_row = np.all(mask, axis=2)

    if np.any(check_col) or np.any(check_row):
        if check_col.sum():
            board_to_check = check_col
        else:
            board_to_check = check_row

        board_index = np.where(board_to_check == 1)[0][0]
        # we are missing some scores in the middle but we don't care
        scores.append(boards[board_index][~mask[board_index]].sum() * num)

        not_winners_mask = np.ones(mask.shape[0], dtype=bool)
        not_winners_mask[np.where(board_to_check == 1)[0]] = 0

        boards = boards[not_winners_mask]
        mask = mask[not_winners_mask]

print("sol_b", scores[-1])
