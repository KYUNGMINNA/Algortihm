def dfs(graph, v, visited):
    # 방문처리
    visited[v] = True

    # DFS 수행
    for i, node in enumerate(graph[v]):
        if i == v or node == 0:
            continue
        if not visited[i]:
            dfs(graph, i, visited)

def solution(n, computers):
    count = 0
    visited = [False] * n
    for i in range(n):
        # 새로운 네트워크가 시작되는 경우
        if not visited[i]:
            dfs(computers, i, visited)
            count += 1
    return print(count)

solution(3,	[[1, 1, 0], [1, 1, 0], [0, 0, 1]])