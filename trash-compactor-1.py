equations = []

with open('advent-of-code-2025/day-6/data/input.txt', 'r') as f:
    for line in f:
        l = line.strip()
        row = l.split(' ')
        while row.__contains__(''):
            row.remove('')
        equations.append(row)

total_answers = 0
for i in range(len(equations[-1])):
    operation = equations[-1][i]
    print(operation)
    equation_answer = 0
    for j in range(len(equations)-1):
        if i >= len(equations[j]):
            continue
        if operation == '+':
            equation_answer += int(equations[j][i])
        elif operation == '*':
            if equation_answer == 0:
                equation_answer = 1
            equation_answer *= int(equations[j][i])
    total_answers += equation_answer
    print(total_answers)

print(total_answers)
