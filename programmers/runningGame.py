def solution(players, callings):
    a = dict()
    i = 0
    for k in players:
        a[k] = i
        i += 1
    for c in callings:
        index = a[c]
        index2 = index-1
        a[c], a[players[index-1]] = index2,index
        players[index], players[index2] = players[index2], players[index]

    return players

# 부르면 그 앞 선수와 바뀌는 로직을 작성함
# 선수를 딕셔너리에 순위로 대입함 대입하고 서로 숫자를 찾아서 바꾸는 로직

player =["mumu", "soe", "poe", "kai", "mine"]
calling =["kai", "kai", "mine", "mine"]

print(solution(player,calling))
