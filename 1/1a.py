if __name__ == "__main__":

    data = [[ch for ch in line if ch.isdigit()] for line in open('1a.txt').read().split('\n')]
    data = ["".join([line[0], line[-1]]) for line in data if line]
    total = sum([int(line) for line in data])

    print(total)
