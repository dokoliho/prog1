def main():
    print(sum_list([4, 7, 1]))


def sum_list(lst):
    total = 0
    for i in lst:
        total += i
    return total


main()
