def solution(numbers, target):
    tree = [0]

    for i in numbers:
        sub = []
        for j in tree:
            sub.append(j + i)
            sub.append(j - i)
        tree = sub

    return print(tree.count(target))

solution([1,1,1,1,1],3)