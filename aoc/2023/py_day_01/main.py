with open("input.txt") as f:
    lines = [line.strip() for line in f.readlines()]


def find_fist_and_last(line: str) -> int:
    digits = [ch for ch in line if ch.isdigit()]
    first = digits[0]
    if len(digits) == 1:
        last = first
    else:
        last = digits[-1]

    number = int(first + last)
    return number


sol_a = sum(find_fist_and_last(line) for line in lines)

print(f"{sol_a = }")

numbers_names = ["one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
numbers = {name: str(i) for i, name in enumerate(numbers_names, 1)}
numbers_reverse = {name[::-1]: i for name, i in numbers.items()}


def check_digit(line: str, numbers: dict[str, str]) -> str:
    for i in range(len(line)):
        chunk = line[i:]
        if chunk[0].isdigit():
            return chunk[0]
        for number in numbers:
            if chunk.startswith(number):
                return numbers[number]


def find_first_digit(line: str) -> str:
    return check_digit(line, numbers)


def find_last_digit(line: str) -> str:
    return check_digit(line[::-1], numbers_reverse)


def find_fist_and_last_2(line: str) -> int:
    first = find_first_digit(line)
    last = find_last_digit(line)
    return int(first + last)


sol_b = sum(find_fist_and_last_2(line) for line in lines)

print(f"{sol_b = }")
