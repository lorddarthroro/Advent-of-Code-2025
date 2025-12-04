total_joltage=0
with open('advent-of-code-2025/day-3/data/input.txt', 'r') as file:
    for line in file:
        line = line.strip()
        digits = [int(c) for c in line]
        largest = max(digits[:len(digits)-1])
        i = digits.index(largest)
        digits = digits[i+1:]
        second_largest = max(digits)
        total_joltage += int(str(largest) + str(second_largest))
        
print(total_joltage)