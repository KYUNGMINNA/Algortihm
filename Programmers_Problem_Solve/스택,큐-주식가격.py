from collections import deque

def solution(prices):
    answer = []
    queue = deque(prices)

    while queue:
        p = queue.popleft()
        sec = 0
        for i in queue:
            sec += 1
            if p > i:
                break
        answer.append(sec)
    return print(answer)


solution([1,2,3,2,3])