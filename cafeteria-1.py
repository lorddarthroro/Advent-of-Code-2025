ranges = []
ingredient_ids = []

with open('advent-of-code-2025/day-5/data/input.txt', 'r') as f:
    for line in f:
        n = line.strip()
        if '-' in n:
            start, end = map(int, n.split('-'))
            ranges.append((start, end))
        elif n != '':
            ingredient_ids.append(int(n))

count = 0
for num in ingredient_ids:
    for start, end in ranges:
        if start <= num <= end:
            count += 1
            break

print("Count of fresh ingredients:", count)
