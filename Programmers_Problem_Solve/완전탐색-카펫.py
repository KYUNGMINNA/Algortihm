def solution(brown, yellow):
    answer = []
    total = brown + yellow
    for h in range(3, total + 1):
        if total % h == 0:
            w = total//h
            if (w - 2) * (h - 2) == yellow:
                answer = [w,h]
                break
    return print(answer)


solution(24,24)