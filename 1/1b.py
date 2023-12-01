def find_occurances(line):
    str_to_digit = {
        'one': 1,
        'two': 2,
        'three': 3,
        'four': 4,
        'five': 5,
        'six': 6,
        'seven': 7,
        'eight': 8,
        'nine': 9
    }

    word_digits = [(i, str_to_digit[num]) for i in range(len(line)) for num in list(str_to_digit.keys()) if line.startswith(num, i)]
    digits = [(i, int(ch)) for i, ch in enumerate(line) if ch.isdigit()]
    all_digits = list(set(word_digits).union(set(digits)))

    return all_digits

if __name__ == "__main__":
    data = [line for line in open('1a.txt').read().split('\n') if line]

    total = 0
    for line in data:
        digits = find_occurances(line)
        digits.sort()
        num = int(str(digits[0][1])+str(digits[-1][1]))
        total += num
    print(total)

