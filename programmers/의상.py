from collections import defaultdict


def solution(clothes):
    a = defaultdict(lambda: 1)
    for cl in clothes:
        a[cl[1]] = a[cl[1]] + 1
    c = 0

    for i in a.keys():
        if c == 0:
            c = a[i]
        else:
            c = c * a[i]

    return c


print(
    solution([["yellow_hat", "headgear"], ["blue_sunglasses", "eyewear"], ["green_turban", "headgear"]])
)
