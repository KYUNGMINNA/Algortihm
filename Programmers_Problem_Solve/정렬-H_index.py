def solution(citations):
    answer = 0

    citations.sort()

    for i in range(len(citations)):
        if citations[i] >= len(citations) - i:
            answer = max(answer, len(citations) - i)

    return print(answer)

solution([3,0,6,1,5])
