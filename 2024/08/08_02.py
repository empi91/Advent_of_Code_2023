import math
from collections import defaultdict

score = 0

area = []
antennas = defaultdict(list)


with open('puzzle_input') as file:
    for line in file:
        area.append(list(line.strip()))


for i, row in enumerate(area):
    for j, char in enumerate(row):
        if char != '.':
            if not antennas[char]:
                antennas[char] = []
            antennas[char].append((i, j))


for antenna_type, antenna_locations in antennas.items():
    for location in antenna_locations:
        for item in antenna_locations:
            if math.dist(location, item) != 0:
                y_diff = location[1] - item[1]
                x_diff = location[0] - item[0]
                a = location[0] + x_diff
                b = location[1] + y_diff
                while a in range(0, len(area)) and b in range(len(area[0])):
                    area[a][b] = "#" 
                    a = a + x_diff
                    b = b + y_diff



for line in area:
    print(line)
    for i in line:
        if i == '#' or i in antennas: score += 1

print(score)