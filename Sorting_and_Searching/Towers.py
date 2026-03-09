import bisect

n = int(input())
cubes = list(map(int, input().split()))

towers = []

for cube in cubes:
    pos = bisect.bisect_right(towers, cube)

    if pos == len(towers):
        towers.append(cube)
    else:
        towers[pos] = cube

print(len(towers))