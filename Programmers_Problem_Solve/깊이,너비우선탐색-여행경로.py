from collections import defaultdict


def solution(tickets):
    graph = defaultdict(list)

    for key, value in tickets:
        graph[key].append(value)


    for g in graph:
        graph[g].sort()

    answer = dfs(graph)

    return print(answer)


# dfs 수행 메서드
def dfs(graph):
    answer = []  #
    stacks = ['ICN']

    while stacks:
        stack = stacks[-1]

        if stack not in graph or len(graph[stack]) == 0:
            answer.append(stacks.pop())
        else:
            stacks.append(graph[stack].pop(0))

    return answer[::-1]

solution([["ICN", "JFK"], ["HND", "IAD"], ["JFK", "HND"]])