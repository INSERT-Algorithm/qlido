from collections import defaultdict


def solution(genres, plays):
    pdict = defaultdict(lambda: [])
    for i in range(len(genres)):
        pdict[genres[i]].append((i, plays[i]))
    pdict = {k: v for k, v in sorted(pdict.items(), key=lambda item: sum(t[1] for t in item[1]), reverse=True)}
    l = list(i[1] for i in pdict.items())
    print(l)
    for i in range(len(l)):
        l[i] = sorted(l[i], key=lambda x: (-x[1], x[0]))
    ls = [i[:2] for i in l]
    li = [j[0] for i in ls for j in i]

    return li


genre = ["classic", "pop", "classic", "classic", "pop"]
play = [500, 600, 150, 800, 2500]

print(solution(genre, play))
