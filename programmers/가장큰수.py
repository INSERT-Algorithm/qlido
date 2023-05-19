from functools import cmp_to_key


def solution(numbers):
    numbers = list(map(str, numbers))
    def compare(a, b):
        if a + b > b + a:
            return -1
        else:
            return 1

    sorted_numbers = sorted(numbers, key=cmp_to_key(compare))
    return str(int(''.join(sorted_numbers)))

n = [3, 30, 34, 5, 9]
print(solution(n))
