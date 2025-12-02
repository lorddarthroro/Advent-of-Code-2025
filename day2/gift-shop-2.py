import textwrap

def contains_repeated_digits(n):
    output = False
    s = str(n)
    length = len(s)
    for w in range (1, length//2 + 1):
        output = True
        wrapped = textwrap.wrap(s, w)
        for i in range(len(wrapped) - 1):
            if wrapped[i] != wrapped[i + 1]:
                output = False
                break
        if output:
            break
    return output

with open('advent-of-code-2025/day-2/data/input.txt', 'r') as file:
    first_line = file.readline()
    # The readline() method often includes the newline character (\n) at the end.
    # You can strip it if not needed.
    first_line_stripped = first_line.strip('\n')

my_list = first_line.split(',')
# print(my_list)
sum_invalid_ids = 0
for item in my_list:
    a, b = item.split('-')
    a = int(a)
    b = int(b)
    for n in range(a, b + 1):
        if contains_repeated_digits(n):
            sum_invalid_ids += n

print(sum_invalid_ids)
