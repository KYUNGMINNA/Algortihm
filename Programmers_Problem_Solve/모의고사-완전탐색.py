def solution(answers):
    a = [1, 2, 3, 4, 5]
    b = [2, 1, 2, 3, 2, 4, 2, 5]
    c = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]
    answer = []
    cnt = [0, 0, 0]

    for i in range(len(answers)):
        if answers[i] == a[(i % len(a))]:
            cnt[0] += 1
        if answers[i] == b[(i % len(b))]:
            cnt[1] += 1
        if answers[i] == c[(i % len(c))]:
            cnt[2] += 1

    for j in range(len(cnt)):
        if cnt[j] == max(cnt):
            answer.append(j + 1)
    return print(sorted(answer))

answers=[1,3,2,4,2]

solution(answers)