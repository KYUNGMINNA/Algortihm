from itertools import permutations
import math


def solution(numbers):
    def numberdetector(number):
        if number < 2:
            return False
        for i in range(2, int(math.sqrt(number)) + 1):
            if number % i == 0:
                return False
        return True

    answers = []

    for i in range(1, len(numbers) + 1):
        for j in list(permutations(numbers, i)):
            k = "".join(j)
            if numberdetector(int(k)):
                answers.append(int(k))
    return print(len(set(answers)))


solution("011")