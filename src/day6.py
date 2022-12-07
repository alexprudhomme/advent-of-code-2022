import helper

path = "/Users/alexprudhomme/Documents/GitHub/advent-of-code-2022/txt_files/day6.txt"


def solve_q1():
    current_threes = []
    lines = helper.open_file(path)
    # line = lines[0]
    line = 'nppdvjthqldpwncqszvftbrmjlhg'
    current_threes.append(line[0])
    current_threes.append(line[1])
    current_threes.append(line[2])
    current_index_to_pop = 0
    for i in range(3, len(line)):
        if line[i] in current_threes:
            current_threes.pop(0)
            current_threes.append(line[i])
        else:
            current_threes.append(line[i])
            if len(current_threes) == 4:
                return i + 1


    return 0


def solve_q2():
    return 0
