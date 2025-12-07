laser_field = []
with open('advent-of-code-2025/day-7/data/input.txt', 'r') as f:  
    for line in f:
        laser_field.append(list(line.strip()))

length = len(laser_field[0])
split_count = 0 

for i in range(len(laser_field)):
    for j in range(length):
        if j > 0 and laser_field[i][j-1] == ('^') and laser_field[i][j] == '.' and laser_field[i-1][j-1] == '|':
            laser_field[i][j] = '|'
            split_count += 1
        elif j < length-1 and i < length and laser_field[i][j+1] == ('^') and laser_field[i][j] == '.' and laser_field[i-1][j+1] == '|':
            laser_field[i][j] = '|' 
            # split_count += 1
        elif i > 0 and laser_field[i-1][j] in ('S', '|') and laser_field[i][j] == '.':
            laser_field[i][j] = '|'
        elif i > 0 and laser_field[i-1][j] == '^':
            laser_field[i][j] = '.'

# for l in laser_field:
#     print(l)
print("Number of splits:", split_count)