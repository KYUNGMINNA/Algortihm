def solution(routes):
    answer = 0
    routes = sorted(routes, key=lambda x: x[1])
    last_camera = -30000

    for i in routes:
        if last_camera < i[0]:
            answer += 1
            last_camera = i[1]

    return print(answer)

solution([[-20,-15], [-14,-5], [-18,-13], [-5,-3]])