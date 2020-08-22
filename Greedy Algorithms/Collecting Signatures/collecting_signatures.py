# python3

from collections import namedtuple
from sys import stdin

Segment = namedtuple('Segment', 'start end')

def compute_optimal_points(segments):
    coordinates = []
    segments.sort(key=lambda x:x.end)
    index = 0
    n = len(segments)
    while index<n:
        curr = segments[index]
        while index < n-1 and curr.end >= segments[index+1].start:
            index +=1
        coordinates.append(curr.end)
        index += 1

    return coordinates


if __name__ == '__main__':
    n, *data = map(int, stdin.read().split())
    input_segments = list(map(lambda x: Segment(x[0], x[1]), zip(data[::2], data[1::2])))
    assert n == len(input_segments)
    output_points = compute_optimal_points(input_segments)
    print(len(output_points))
    print(*output_points)
