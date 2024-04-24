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

def make_map(d: int, s: int, z: int):
    return {i + s: i + d for i in range(z)}


map1 = make_map(50, 98, 2)

print(map1)
print(map1[99])
