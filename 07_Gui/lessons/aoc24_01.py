from time import perf_counter as pfc


def read_puzzle(filename):
    with open(filename) as file:
        return [line.strip() for line in file]


def solve_part_1():
    puzzle = read_puzzle("puzzle_input.txt")
    left, right = split_puzzle(puzzle)
    left.sort()
    right.sort()
    distances = calculate_distances(left, right)
    return sum(distances)


def solve_part_2():
    puzzle = read_puzzle("puzzle_input.txt")
    left, right = split_puzzle(puzzle)
    similarity_scores = calculate_similarity_scores(left, right)
    return sum(similarity_scores)


def calculate_distances(left, right):
    differences = []
    for i in range(len(left)):
        differences.append(abs(left[i] - right[i]))

    return differences


def calculate_similarity_scores(left, right):
    right_counts = {}
    for num in right:
        if num in right_counts:
            right_counts[num] += 1
        else:
            right_counts[num] = 1
    scores = []
    for num in left:
        if num not in right_counts:
            scores.append(0)
        else:
            scores.append(right_counts[num] * num)
    return scores


def split_puzzle(puzzle):
    left = []
    right = []
    for line in puzzle:
        parts = line.split()  # Split the line into two parts
        left.append(int(parts[0]))  # Add the first number to the left list
        right.append(int(parts[1]))  # Add the second number to the right list
    return left, right


if __name__ == "__main__":
    # Solve part 1 and print the result
    start = pfc()
    result1 = solve_part_1()
    print(f"Part 1: {result1} ({pfc() - start:.4f}s)")

    # Solve part 2 and print the result
    start = pfc()
    result2 = solve_part_2()
    print(f"Part 2: {result2} ({pfc() - start:.4f}s)")