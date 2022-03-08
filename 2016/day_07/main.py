from itertools import chain


def read_data(path_data: str) -> list[str]:
    with open(path_data) as f:
        return [line.strip() for line in f.readlines()]


def process_raw_line(line: str) -> list[str]:
    return line.replace("[", " ").replace("]", " ").split()


def has_tls(chunk: str) -> bool:
    len_chunk = len(chunk)
    for i in range(len_chunk - 3):
        windows = chunk[i : i + 4]
        if windows[0] != windows[1] and windows[:2] == windows[2:][::-1]:
            return True
    return False


def is_valid_tls(ip: list[str]) -> bool:
    for chunk in ip[1::2]:
        if has_tls(chunk):
            return False
    if any(has_tls(chunk) for chunk in ip[::2]):
        return True
    return False


def has_ssl(chunk: str, reverse_output: bool = False) -> list[str]:
    len_chunk = len(chunk)
    candidates = []
    for i in range(len_chunk - 2):
        windows = chunk[i : i + 3]
        if windows[0] != windows[1] and windows[0] == windows[-1]:
            if reverse_output:
                windows = windows[1] + windows[0] + windows[1]
            candidates.append(windows)
    return candidates


def is_valid_ssl(ip: list[str]) -> bool:
    aba = list(chain(*[has_ssl(chunk) for chunk in ip[::2]]))
    bab_reversed = list(
        chain(*[has_ssl(chunk, reverse_output=True) for chunk in ip[1::2]])
    )
    for i in aba:
        if i in bab_reversed:
            return True
    return False


if __name__ == "__main__":
    data = [process_raw_line(line) for line in read_data("input.txt")]

    sol_a = sum(is_valid_tls(ip) for ip in data)
    print(f"sol_a: {sol_a}")

    sol_b = sum(is_valid_ssl(ip) for ip in data)
    print(f"sol_b: {sol_b}")


def test_is_valid_tls():
    test_data_tls = [
        ("abba[mnop]qrst", True),
        ("abcd[bddb]xyyx", False),
        ("aaaa[qwer]tyui", False),
        ("ioxxoj[asdfgh]zxcvbn", True),
    ]
    for raw_line, result in test_data_tls:
        assert is_valid_tls(process_raw_line(raw_line)) == result


def test_is_valid_ssl():
    test_data_ssl = [
        ("aba[bab]xyz", True),
        ("xyx[xyx]xyx", False),
        ("aaa[kek]eke", True),
        ("zazbz[bzb]cdb", True),
    ]
    for raw_line, result in test_data_ssl:
        assert is_valid_ssl(process_raw_line(raw_line)) == result
