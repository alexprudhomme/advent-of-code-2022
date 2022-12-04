import helper


def solve_q1() -> int:
    lines = helper.open_file('/Users/alexprudhomme/Documents/GitHub/AdventOfCode/day4.txt')
    sum_fully_contain = 0
    for s in lines:
        two_elves = s.split(',')
        first_elf = two_elves[0].split('-')
        second_elf = two_elves[1].split('-')
        if (int(first_elf[0]) <= int(second_elf[0]) and int(first_elf[1]) >= int(second_elf[1])) or (
                int(first_elf[0]) >= int(second_elf[0]) and int(first_elf[1]) <= int(second_elf[1])):
            sum_fully_contain += 1
    return sum_fully_contain


def solve_q2() -> int:
    lines = helper.open_file('/Users/alexprudhomme/Documents/GitHub/AdventOfCode/day4.txt')
    sum_overlap = 0
    for s in lines:
        two_elves = s.split(',')
        first_elf = two_elves[0].split('-')
        second_elf = two_elves[1].split('-')
        first_elf_start = int(first_elf[0])
        first_elf_end = int(first_elf[1])
        second_elf_start = int(second_elf[0])
        second_elf_end = int(second_elf[1])
        if (second_elf_start <= first_elf_start <= second_elf_end) or (
                second_elf_end >= first_elf_end >= second_elf_start) or (int(first_elf[0]) <= int(second_elf[0]) and int(first_elf[1]) >= int(second_elf[1])) or (
                int(first_elf[0]) >= int(second_elf[0]) and int(first_elf[1]) <= int(second_elf[1])):
            sum_overlap += 1
    return sum_overlap
