def visualize_tiles(red_tiles, green_tiles):
    for j in range(14):
        row = "."
        for i in range(14):
            if (i, j) in red_tiles:
                row += "R "
            elif (i, j) in green_tiles:
                row += "G "
            else:
                row += ". "
        print(row)

def get_greed_tiles(red_tiles):
    # outline green tiles
    green_tiles = []
    red_tiles = set(red_tiles)
    for tile in red_tiles:
        for tile2 in red_tiles:
            if tile != tile2:
                if tile[0] == tile2[0]:
                    for y in range(min(tile[1], tile2[1]) + 1, max(tile[1], tile2[1])):
                        green_tiles.append((tile[0], y))
                elif tile[1] == tile2[1]:
                    for x in range(min(tile[0], tile2[0]) + 1, max(tile[0], tile2[0])):
                        green_tiles.append((x, tile[1]))
    green_tiles = set(green_tiles) 
    blocked = red_tiles | green_tiles
    # fill green tiles
    xs = [x for x,y in blocked]
    ys = [y for x,y in blocked]
    min_x, max_x = min(xs)-1, max(xs)+1
    min_y, max_y = min(ys)-1, max(ys)+1

    start = (min_x, min_y)
    outside = {start}
    stack = [start]

    while stack:
        x, y = stack.pop() 

        for nx, ny in [(x+1,y),(x-1,y),(x,y+1),(x,y-1)]:
            if (nx,ny) in outside:
                continue
            if nx < min_x or nx > max_x or ny < min_y or ny > max_y:
                continue
            if (nx,ny) in blocked:
                continue

            outside.add((nx,ny))
            stack.append((nx,ny))

    for x in range(min_x, max_x+1):
        for y in range(min_y, max_y+1):
            if (x,y) not in outside and (x,y) not in red_tiles:
                green_tiles.add((x,y))

    return green_tiles

def check_colors_valid(tile1, tile2, red_tiles, green_tiles):
    red_tiles = set(red_tiles)
    green_tiles = set(green_tiles)
    green = False
    red = False
    for i in range(min(tile1[0], tile2[0]), max(tile1[0], tile2[0])+1):
        for j in range(min(tile1[1], tile2[1]), max(tile1[1], tile2[1])+1):
            if (i, j) not in green_tiles and (i, j) not in red_tiles:
                return False
    return True

def manhattan_distance(x, y):
    return abs(x[0] - y[0]) + abs(x[1] - y[1])

def find_biggest_area_p1(red_tiles, green_tiles):
    biggest_distance = 0
    furthest_pair = None

    for tile in red_tiles:
        for tile2 in red_tiles:
            if manhattan_distance(tile, tile2) > biggest_distance and check_colors_valid(tile, tile2, red_tiles, green_tiles):
                biggest_distance = manhattan_distance(tile, tile2)
                furthest_pair = (tile, tile2)
    length = abs(furthest_pair[0][0] - furthest_pair[1][0]) + 1
    width = abs(furthest_pair[0][1] - furthest_pair[1][1]) + 1
    area = abs(length * width)
    return area

red_tiles = []
with open('advent-of-code-2025/day-9/data/input0.txt', 'r') as f:  
    for line in f:
        numbers =line.strip().split(',')
        red_tiles.append((int(numbers[0]), int(numbers[1])))

green_tiles = get_greed_tiles(red_tiles)


print(find_biggest_area_p1(red_tiles, green_tiles))


# visualize_tiles(red_tiles, green_tiles)
