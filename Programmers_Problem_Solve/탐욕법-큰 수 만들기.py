def solution(number, k):
    answer = []

    for i in number:
        while k > 0 and answer and answer[-1] < i:
            answer.pop()
            k -= 1
        answer.append(i)

    return print(''.join(answer[:len(answer) - k]))
number="4177252841"
k=4
solution(number,k)