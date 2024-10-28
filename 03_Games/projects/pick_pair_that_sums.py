
def main():
    print("Dieses Programm sucht ein Paar von Zahlen in einer Liste, die zusammen eine gegebene Summe ergeben.")
    lst = [1, 2, 3, 4, 5]
    target = 7
    result = two_sum(lst, target)
    if result:
        print(f"Das Paar von Zahlen, die zusammen {target} ergeben, ist {result}.")
    else:
        print(f"Es gibt kein Paar von Zahlen, die zusammen {target} ergeben.")


def length(lst):
    # return len(lst)
    count = 0
    for _ in lst:
        count += 1
    return count


def two_sum(lst, target):
    for i in range(length(lst)):
        j = i+1
        while j < length(lst):
            if lst[i] + lst[j] == target:
                return (lst[i], lst[j])
            j += 1
    return None


main()
