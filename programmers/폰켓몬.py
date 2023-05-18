def solution(nums):
    a = dict.fromkeys(nums, 0)
    MAX = len(nums) / 2
    if len(a.keys()) > MAX:
        return MAX
    else:
        return int(len(a.keys()))


#해쉬문제 딕셔너리로 처리한 후에 최대 로 가질 수 있는 범위를 MAX에 대입
# 딕셔너리 key의 갯수가 그거보다 크면 무조건 MAX 아니라면 key의 길이를 출력

print(solution([3, 1, 2, 3]) == 2)
print(solution([3, 3, 3, 2, 2, 4]) == 3)
print(solution([3, 3, 3, 2, 2, 2]) == 2)
