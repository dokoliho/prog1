
def main():
    print("Dieses Programm sucht ein Paar von Zahlen in einer Liste, die zusammen eine gegebene Summe ergeben.")
    lst = [1, 2, 3, 4, 5]
    target = 7
    result = two_sum(lst, target)
    if result:
        print(f"Das Paar von Zahlen, die zusammen {target} ergeben, ist {result}.")
    else:
        print(f"Es gibt kein Paar von Zahlen, die zusammen {target} ergeben.")


def two_sum(lst, target):
    n = length(lst)
    for i in range(n):
        j = i+1
        while j < n:
            if lst[i] + lst[j] == target:
                # Rückgabe als Tupel mit den beiden gefundenen Zahlen
                return (lst[i], lst[j])
            j += 1
    return None


def length(lst):
    # return len(lst)
    count = 0
    for _ in lst:
        count += 1
    return count


main()
