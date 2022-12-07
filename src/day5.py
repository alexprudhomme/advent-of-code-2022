import helper

path = '/Users/alexprudhomme/Documents/GitHub/AdventOfCode/day5i.txt'


def solve_q1() -> str:
    stacks = [
        ['D', 'T', 'R', 'B', 'J', 'L', 'W', 'G'],
        ['S', 'W', 'C'],
        ['R', 'Z', 'T', 'M'],
        ['D', 'T', 'C', 'H', 'S', 'P', 'V'],
        ['G', 'P', 'T', 'L', 'D', 'Z'],
        ['F', 'B', 'R', 'Z', 'J', 'Q', 'C', 'D'],
        ['S', 'B', 'D', 'J', 'M', 'F', 'T', 'R'],
        ['L', 'H', 'R', 'B', 'T', 'V', 'M'],
        ['Q', 'P', 'D', 'S', 'V']
    ]
    lines = helper.open_file(path)
    for l in lines:
        words = l.split(' ')
        for i in range(int(words[1])):
            value = stacks[int(words[3]) - 1].pop()
            stacks[int(words[5]) - 1].append(value)
    answer = ''
    for i in range(len(stacks)):
        answer += stacks[i].pop()
    # make all stacks
    # depending on order pop and pull
    return answer


def solve_q2() -> str:
    stacks = [
        ['D', 'T', 'R', 'B', 'J', 'L', 'W', 'G'],
        ['S', 'W', 'C'],
        ['R', 'Z', 'T', 'M'],
        ['D', 'T', 'C', 'H', 'S', 'P', 'V'],
        ['G', 'P', 'T', 'L', 'D', 'Z'],
        ['F', 'B', 'R', 'Z', 'J', 'Q', 'C', 'D'],
        ['S', 'B', 'D', 'J', 'M', 'F', 'T', 'R'],
        ['L', 'H', 'R', 'B', 'T', 'V', 'M'],
        ['Q', 'P', 'D', 'S', 'V']
    ]
    lines = helper.open_file(path)
    for l in lines:
        words = l.split(' ')

        from_line = stacks[int(words[3]) - 1]
        to_line = stacks[int(words[5]) - 1]
        slice = from_line[-(int(words[1])):]
        # remove
        for i in range(int(words[1])):
            stacks[int(words[3]) - 1].pop()
        stacks[int(words[5]) -1].extend(slice)
    answer = ''
    for i in range(len(stacks)):
        answer += stacks[i].pop()
    # make all stacks
    # depending on order pop and pull
    return answer
