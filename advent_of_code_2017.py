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


# Day 2, part 1

def check_spreadsheet_sum(sheet):
    """Return the checksum for a spreadsheet.

    Instructions:
    "For each row, determine the difference between the largest value and the 
     smallest value; the checksum is the sum of all of these differences."

    >>> sheet = "data/day2_test_data.txt"
    >>> check_spreadsheet_sum(sheet)
    18
    """

    checksum = 0

    with open(sheet) as spreadsheet:
        for row in spreadsheet:
            row = row.rstrip().split()
            row = [int(num) for num in row]

            largest = max(row)
            smallest = min(row)

            checksum = checksum + (largest - smallest)

    return checksum


# Day 2, part 2

def check_spreadsheet_sum2(sheet):
    """Return the checksum for a spreadsheet.

    Instructions:
    "Find the only two numbers in each row where one evenly divides the other.
    That is, where the result of the division operation is a whole number. Find
    those numbers on each line, divide them, and add up each line's result."

    >>> sheet = "data/day2_part2_test_data.txt"
    >>> check_spreadsheet_sum2(sheet)
    9
    """

    checksum = 0

    with open(sheet) as spreadsheet:
        for row in spreadsheet:
            row = row.rstrip().split()
            row = [int(num) for num in row]

            for i in range(len(row) - 1):
                for j in range(i + 1, len(row)):
                    num1 = row[i]
                    num2 = row[j]

                    if num1 % num2 == 0:
                        checksum = checksum + (num1 / num2)

                    elif num2 % num1 == 0:
                        checksum = checksum + (num2 / num1)

    return checksum
