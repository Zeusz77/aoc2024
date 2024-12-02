def __main__():
    with open("input.txt") as f:
        lines = f.readlines()

    first_column = []
    second_column = []

    total = 0
    for line in lines:
        a, b = line.split()
        first_column.append(int(a))
        second_column.append(int(b))

    first_column.sort()
    second_column.sort()

    for i in range(len(first_column)):
        if first_column[i] >= second_column[i]:
            total += first_column[i] - second_column[i]
        else:
            total += second_column[i] - first_column[i]

    print(total)

if __name__ == "__main__":
    __main__()