"""
Consider again the example seed-to-soil map:

dest source size
  50     98    2
  52     50   48

The first line has a destination range start of 50, a source range start of 98, and
a range length of 2. This line means that the source range starts at 98 and contains
two values: 98 and 99. The destination range is the same length, but it starts at 50,
so its two values are 50 and 51. With this information, you know that seed number 98
corresponds to soil number 50 and that seed number 99 corresponds to soil number 51.
"""

from typing import Sequence, Tuple


def get_row(txt: str):
    return [int(num) for num in txt.split(" ")]


def get_map_nums(seq: Sequence[str]):
    nums = []
    for i, txt in enumerate(seq):
        if not txt.strip():
            return i, nums
        nums.append(get_row(txt.strip()))

    return i, nums


class Map:

    def __init__(self, rows: Sequence[Tuple[int, int, int]]):
        self.rows = rows

    # dest source size
    def __getitem__(self, i):
        for dest, source, size in self.rows:
            if i < source:
                continue
            ub = source + size
            if i < ub:
                delta = i - source
                return dest + delta
        return i


def test1():
    pos = 3
    lines = test_input.splitlines()
    i, seed2soil_nums = get_map_nums(lines[pos:])
    map1 = Map(seed2soil_nums)
    assert map1[0] == 0
    assert map1[1] == 1
    assert map1[48] == 48
    assert map1[49] == 49
    assert map1[50] == 52
    assert map1[51] == 53
    assert map1[96] == 98
    assert map1[97] == 99
    assert map1[98] == 50
    assert map1[99] == 51
    print("test1 ok")


input = "input5.txt"
with open(input, "r") as file:
    lines = file.readlines()


pos = 0
things = get_row(lines[pos][7:])
print(things)
print(lines[2])


def get_next_things(lines, pos, things):
    i, map_nums = get_map_nums(lines[pos:])
    map = Map(map_nums)
    pos += i + 2
    things = [map[i] for i in things]
    return pos, things


pos = 3

while pos < len(lines):
    pos, things = get_next_things(lines, pos, things)

print(f"min location is: {min(things)}")
