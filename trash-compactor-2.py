with open('advent-of-code-2025/day-6/data/input.txt') as f:
    rows = [line.rstrip('\n') for line in f]

# Pad to equal width
width = max(len(r) for r in rows)
rows = [r.ljust(width) for r in rows]

# Build columns, right-to-left
columns = []
for col_index in range(width - 1, -1, -1):
    column = [rows[row_index][col_index] for row_index in range(len(rows))]
    columns.append(column)

numbers = []
for i in range(len(columns)):
    num = ''
    operation = ''
    for j in range(len(columns[i])):
        # print(columns[i][j])
        if columns[i][j] == ' ':
            continue
        elif columns[i][j] == '+':
            operation = '+'
        elif columns[i][j] == '*':
            operation = '*'
        else:
            num = num + (columns[i][j])
    numbers.append(num)
    if operation != '':
        numbers.append(operation)
while '' in numbers:
    numbers.remove('')
# print(numbers)

total_answer = 0
answer = 0
operation = ''
for i in range(len(numbers)-1, -1, -1):
    if numbers[i] in '+*':
        operation = numbers[i]
        total_answer += answer
        answer = 0
    else:
        if answer == 0:
            answer = int(numbers[i])
        else:
            if operation == '+':
                answer += int(numbers[i])
            elif operation == '*':
                answer *= int(numbers[i])

total_answer += answer

print(total_answer)
