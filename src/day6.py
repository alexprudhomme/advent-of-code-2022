import helper

path = "/Users/alexprudhomme/Documents/GitHub/advent-of-code-2022/txt_files/day6.txt"


def uniqueCharacters(st):
    # Using sorting
    st = sorted(st)

    for i in range(len(st) - 1):

        # if at any time, 2 adjacent
        # elements become equal,
        # return false
        if (st[i] == st[i + 1]):
            return False

    return True

def solve_q1():
    current_threes = []

    lines = helper.open_file(path)
    line = lines[0]
    current_threes.append(line[0])
    current_threes.append(line[1])
    current_threes.append(line[2])
    current_threes.append(line[3])
    current_index_to_pop = 0
    for i in range(4, len(line)):
        if uniqueCharacters(''.join(current_threes)):
            return i
        else:
            current_threes.pop(0)
            current_threes.append(line[i])
    return 0


def solve_q2():
    current_threes = []

    lines = helper.open_file(path)
    line = lines[0]
    current_threes.append(line[0])
    current_threes.append(line[1])
    current_threes.append(line[2])
    current_threes.append(line[3])
    current_threes.append(line[4])
    current_threes.append(line[5])
    current_threes.append(line[6])
    current_threes.append(line[7])
    current_threes.append(line[8])
    current_threes.append(line[9])
    current_threes.append(line[10])
    current_threes.append(line[11])
    current_threes.append(line[12])
    current_threes.append(line[13])
    for i in range(14, len(line)):
        if uniqueCharacters(''.join(current_threes)):
            return i
        else:
            current_threes.pop(0)
            current_threes.append(line[i])
    return 0
