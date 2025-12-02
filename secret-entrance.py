position=50
zero_counter = 0
with open('advent-of-code-2025/day-1/data/input0.txt', 'r') as file:
    for line in file:
        line = line.strip()
        # line = file.readline()
        if not line:  # skip empty lines
            continue
        if line[0] == 'R':
            position = (position + int(line[1:])) % 100
        else:
            position = (position - int(line[1:])) % 100
        if position == 0:
            zero_counter+=1
        print(line + ": " + str(position))

print(zero_counter)

