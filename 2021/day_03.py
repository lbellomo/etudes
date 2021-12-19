from collections import Counter

Data = list[str]

with open("inputs/day_03.txt") as f:
    data = [line.strip() for line in f.readlines()]

counter_list = []
for i in range(len(data[0])):
    counter = Counter([row[i] for row in data])
    counter_list.append(counter)

gamma_str = "".join(counter.most_common()[0][0] for counter in counter_list)
epsilon_str = "".join(counter.most_common()[-1][0] for counter in counter_list)

print("sol_a", int(gamma_str, 2) * int(epsilon_str, 2))


def find_common(data: Data, index: int, by_most_common: bool) -> str:
    counter = Counter([row[index] for row in data])
    if len(set(i[1] for i in counter.most_common())) == 1:
        if by_most_common:
            return "1"
        else:
            return "0"
    else:
        if by_most_common:
            return counter.most_common()[0][0]
        else:
            return counter.most_common()[-1][0]


def filter_by_common(data: Data, by_most_common: bool) -> str:
    data_tmp = data[:]
    len_row = len(data_tmp[0])

    for i in range(len_row):
        next_filter = find_common(data_tmp, i, by_most_common=by_most_common)
        data_tmp = [row for row in data_tmp if row[i] == next_filter]
        if len(data_tmp) == 1:
            break

    return data_tmp[0]


oxygen_generator_rating = filter_by_common(data, by_most_common=True)
CO2_scrubber_rating = filter_by_common(data, by_most_common=False)
print("sol_b", int(oxygen_generator_rating, 2) * int(CO2_scrubber_rating, 2))
