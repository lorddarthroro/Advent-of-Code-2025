array_2d = []
count = 0
with open('advent-of-code-2025/day-4/data/input0.txt', 'r') as f:
    for line in f:
        array_2d.append(list(line.strip()))  # read characters
        

for i in range(len(array_2d)):
    for j in range(len(array_2d[i])):
        
        if array_2d[i][j] != "@":
            continue

        number_of_neighbors = 0
        
        for di in [-1, 0, 1]:
            for dj in [-1, 0, 1]:
                if di == 0 and dj == 0:
                    continue

                ni, nj = i + di, j + dj

                if 0 <= ni < len(array_2d) and 0 <= nj < len(array_2d[0]):
                    if array_2d[ni][nj] == "@":
                        number_of_neighbors += 1
        if number_of_neighbors < 4:
            count += 1

print(count)
