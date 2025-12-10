from itertools import combinations


from itertools import combinations

def find_solution(pattern, buttons):
    n_buttons = len(buttons)
    num_lights = len(pattern)

    for depth in range(1, n_buttons + 1):
        for combo in combinations(range(n_buttons), depth):
            initial = [0] * num_lights
            result = press_buttons(initial, buttons, combo)
            if result == pattern:
                return depth 

    return None


def press_buttons(state, buttons, combo):
    new_pattern = state.copy()
    for b in combo:
        for pos in buttons[b]:
            new_pattern[pos] = (new_pattern[pos] + 1) % 2
    return new_pattern


all_patterns = []
all_buttons = []
all_jolts = []

with open('advent-of-code-2025/day-10/data/input.txt', 'r') as f:
    for line in f:
        line = line.strip()
        if not line:
            continue

        pattern_str = line.split('[',1)[1].split(']',1)[0]
        pattern = [1 if c == '#' else 0 for c in pattern_str]

        mid = line.split(']',1)[1].split('{',1)[0].strip()
        button_parts = [x.strip() for x in mid.split() if x.startswith('(')]

        buttons = []
        for part in button_parts:
            nums = part.strip('()')
            if nums == "":
                buttons.append(())
            else:
                buttons.append(tuple(int(n) for n in nums.split(',')))

        jolts_str = line.split('{',1)[1].split('}',1)[0]
        jolts = [int(x) for x in jolts_str.split(',')]
        all_patterns.append(pattern)
        all_buttons.append(buttons)
        all_jolts.append(jolts)

total = 0
for i in range(len(all_patterns)):
    pattern = all_patterns[i]
    buttons = all_buttons[i]
    jolts = all_jolts[i]
    total += find_solution(pattern, buttons)
print(total)
