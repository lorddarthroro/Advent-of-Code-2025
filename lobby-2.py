total_joltage=0
with open('advent-of-code-2025/day-3/data/input.txt', 'r') as file:
    for line in file:
        voltage = ''
        line = line.strip()
        digits = [int(c) for c in line]
        for n in range(12):
            needed = 12 - len(voltage)
            max_index = len(digits) - needed   # inclusive

            search_space = digits[:max_index+1]
            largest = max(search_space)
            i = search_space.index(largest)
            i = digits.index(largest)
            digits = digits[i+1:]
            voltage += str(largest)

        total_joltage += int(voltage)
print(total_joltage)