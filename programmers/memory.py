def solution(name, yearning, photo):
    a = dict(zip(name, yearning))
    b = []
    for ph in photo:
        b.append(sum(list(a.get(p,0) for p in ph)))

    return b


# name과 yearing이 있는 배열 두개를 묶어 딕셔너리로 변환
# for 문으로 photo 배열이 2차원 이기 때문에 하나씩 돌려서 배열 단위로 분리후
# get함수로 값이 없다면 0 을 받아서 더해서 정답 배열에 추가함

name = ["may", "kein", "kain", "radi"]
yearning = [5, 10, 1, 3]
photo = [["may", "kein", "kain", "radi"], ["may", "kein", "brin", "deny"], ["kon", "kain", "may", "coni"]]
result = [19, 15, 6]

print(solution(name, yearning, photo) == result)
