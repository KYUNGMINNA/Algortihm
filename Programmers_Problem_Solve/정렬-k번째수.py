def solution(array, commands):
    answer = []

    for i in range(len(commands)):
        arr_list = array[commands[i][0]-1:commands[i][1]]
        arr_list.sort()
        print(arr_list)
        answer.append(arr_list[commands[i][2]-1])
    return print(answer)

solution([1, 5, 2, 6, 3, 7, 4],[[2, 5, 3], [4, 4, 1], [1, 7, 3]])