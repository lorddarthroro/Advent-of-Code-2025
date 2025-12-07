def count_timelines(laser_field):
    from functools import lru_cache

    rows = len(laser_field)
    cols = len(laser_field[0])

    start_col = laser_field[0].index('S')

    @lru_cache(maxsize=None) # caching speeds up a ridiculous amount, takes way too long without it
    def dfs(r, c):
        if r >= rows:
            return 1  
        cell = laser_field[r][c]
        if cell == '.':
            return dfs(r + 1, c) 
        elif cell == '^':
            count = 0
            if c > 0:  
                count += dfs(r + 1, c - 1)
            if c < cols - 1: 
                count += dfs(r + 1, c + 1)
            return count
        else:
            return dfs(r + 1, c)

    return dfs(0, start_col)


laser_field = []
with open('advent-of-code-2025/day-7/data/input.txt', 'r') as f:  
    for line in f:
        laser_field.append(list(line.strip()))

print(count_timelines(laser_field))