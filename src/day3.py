def solve_q1() -> int:
    with open('day3.txt') as f:
        lines = f.readlines()

    new_lines = [item.strip() for item in lines]
    sum = 0
    for s in new_lines:
        first_half = s[slice(0, len(s) // 2)]
        second_half = s[slice(len(s) // 2, len(s))]
        letter_in_common = ''.join(set(first_half).intersection(second_half))
        if letter_in_common.isupper():
            sum += ord(letter_in_common) - 38
        else:
            sum += ord(letter_in_common) - 96
    return sum


def solve_q2() -> int:
    with open('day3.txt') as f:
        lines = f.readlines()

    new_lines = [item.strip() for item in lines]
    sum = 0
    index = 0
    index_of_new_list = 0
    small_list = []
    big_list = []
    for s in new_lines:
        if index == 2:
            index = 0
            small_list.append(s)
            big_list.append(small_list)
            # add to new list with index of new list
            small_list = []
            index_of_new_list += 1
        else:
            small_list.append(s)
            index += 1
            #add to small list

    for s in big_list:
        common = set.intersection(*map(set, s))
        letter = common.pop()
        if letter.isupper():
            sum += ord(letter) - 38
        else:
            sum += ord(letter) - 96

    return sum


print(solve_q2())
