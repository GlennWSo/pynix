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


class Line:
    def __init__(self, dest, source, size):
        self.dest = dest
        self.source = source
        self.size = size

    @classmethod
    def mk_lines(cls, seq: Sequence[Tuple[int, int, int]]):
        return [cls(d, s, z) for (d, s, z) in seq]


def lines2map(lines: Sequence[Line]):
    map = {}
    for line in lines:
        for i in range(line.size):
            map[line.source + i] = line.dest + i

    return map


class Map:
    def __init__(self, lines: Sequence[Line]):
        self.map = lines2map(lines)

    @classmethod
    def from_seq(cls, seq: Sequence[Tuple[int, int, int]]):
        return cls(Line.mk_lines(seq))

    def __getitem__(self, i):
        try:
            return self.map[i]
        except KeyError:
            return i

    def __repr__(self):
        return repr(self.map)


seed2soil = [
    (50, 98, 2),
    (52, 50, 48),
]

map1 = Map.from_seq(seed2soil)

seeds = [
    0,
    1,
    48,
    49,
    50,
    51,
    96,
    97,
    98,
    99,
]

for i in seeds:
    print(f"{i}: {map1[i]}")

assert map1[79] == 81
assert map1[14] == 14
assert map1[55] == 57
assert map1[13] == 13

print("all done!")
