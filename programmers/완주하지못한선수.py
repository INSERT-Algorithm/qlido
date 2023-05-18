# import collections
# def solution(participant, completion):
#     participant.sort()
#     completion.sort()
#     a = collections.Counter(participant)
#     b = collections.Counter(completion)
#     return list(a-b)[0]

def solution(participant, completion):
    temp = 0
    dic = dict()
    for part in participant:
        dic[hash(part)] = part
        temp += int(hash(part))
    for com in completion:
        temp -= hash(com)
    return dic[temp]

# 고유한 값인 hash를 이용해서 모두 더하고 뺸후 dict에서 찾아 리턴함

participant	= ["leo", "kiki", "eden"]
completion = ["eden", "kiki"]

print(solution(participant,completion))