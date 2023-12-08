from typing import NamedTuple

with open("input.txt") as f:
    raw_data = f.read()


class MapRange(NamedTuple):
    src: range
    dest: range


def build_map_range(*values):
    dest_start, src_start, length = values
    return MapRange(
        range(src_start, src_start + length), range(dest_start, dest_start + length)
    )


def translate(seed, category_map):
    for map_range in category_map:
        if seed in map_range.src:
            index = map_range.src.index(seed)
            return map_range.dest[index]
    return seed


(raw_seeds,), *raw_maps = [chunk.splitlines() for chunk in raw_data.split("\n\n")]
seeds = [int(i) for i in raw_seeds.strip("seeds:").split()]
maps = [
    [build_map_range(*(int(i) for i in line.split())) for line in values]
    for _title, *values in raw_maps
]

tmp_seeds = seeds

for category_map in maps:
    tmp_seeds = [translate(seed, category_map) for seed in tmp_seeds]
    # print(tmp_seeds)

sol_a = min(tmp_seeds)
print(f"{sol_a = }")


class Range(NamedTuple):
    start: int
    end: int


def overlap(sr: Range, m: MapRange) -> bool:
    seed_start_in = sr.start in m.src and sr.end not in m.src
    seed_stop_in = sr.end in m.src and sr.start not in m.src
    src_in_seed = sr.start < m.src.start and (m.src.stop - 1) < (sr.end)
    return seed_start_in or seed_stop_in or src_in_seed


def inside(sr: Range, m: MapRange) -> bool:
    return m.src.start <= sr.start <= sr.end <= (m.src.stop - 1)


def split(sr: Range, m: MapRange) -> list[Range]:
    # seed_start_in
    if sr.start in m.src and sr.end not in m.src:
        return [Range(sr.start, m.src.stop - 1), Range(m.src.stop, sr.end)]
    # seed_stop_in
    elif sr.end in m.src and sr.start not in m.src:
        return [Range(sr.start, m.src.start - 1), Range(m.src.start, sr.end)]
    # src_in_seed
    elif sr.start < m.src.start and (m.src.stop - 1) < (sr.end):
        return [
            Range(sr.start, m.src.start - 1),
            Range(m.src.start, m.src.stop - 1),
            Range(m.src.stop, sr.end),
        ]
    else:
        raise ValueError("Invalid, this is a bug")


init_seeds = [
    Range(start, start + length - 1) for start, length in zip(seeds[::2], seeds[1::2])
]
s = init_seeds[:]

for i, category_map in enumerate(maps):
    final_s = list()

    while s:
        sr = s.pop()
        if any(inside(sr, m) for m in category_map):
            final_s.append(sr)
        elif not any(overlap(sr, m) for m in category_map):
            final_s.append(sr)
        else:
            for m in category_map:
                if overlap(sr, m):
                    sr_splited = split(sr, m)
                    break

            for sr in sr_splited:
                s.append(sr)
    # tranlate map
    s = [
        Range(translate(sr.start, category_map), translate(sr.end, category_map))
        for sr in final_s
    ]
    # print(s)

sol_b = min(sr.start for sr in s)
print(f"{sol_b = }")
