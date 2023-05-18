def solution(array, commands):
    answer = []
    for c in commands:
        i, j, k = c
        ta = array[i-1:j]
        ta.sort()
        answer.append(ta[k-1])

    return answer

# i, j 까지 잘랐을때 k 번째 수 구하기
# for문으로 command 수 만큼 처리하고 i,j 자른 후에 k번쨰 를 구해 정답 배열에 추가함

arr = [1, 5, 2, 6, 3, 7, 4]
cmd = [[2, 5, 3], [4, 4, 1], [1, 7, 3]]
print(solution(arr, cmd))
