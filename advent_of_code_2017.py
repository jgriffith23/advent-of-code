"""Solutions to advent of code 2017."""

# Day 1, part 1

def check_sum(n_str):
    """Return sum of all digits that match the next digit in the list.

       >>> check_sum("1122")
       3
       >>> check_sum("1111")
       4
       >>> check_sum("1234")
       0
       >>> check_sum("91212129")
       9
    """

    acc = 0
    prev = None
    for curr in n_str:
        if curr == prev:
            acc = acc + int(curr)
        prev = curr
    if prev == n_str[0]:
        acc = acc + int(prev)
    return acc

# Day 1, part 2

def check_sum_2(n_str):
    """Return sum of all digits that match the digit len/2 away in the list.

       >>> check_sum_2("1212")
       6
       >>> check_sum_2("1221")
       0
       >>> check_sum_2("123425")
       4
       >>> check_sum_2("12131415")
       4
    """

    accumulator = 0

    for i in range(len(n_str)):
        curr = n_str[i]
        if i >= len(n_str) / 2:
            check_idx = i - (len(n_str) / 2)

        else:
            check_idx = i + (len(n_str)/2)

        if curr == n_str[check_idx]:
            accumulator = accumulator + int(curr)

    return accumulator
