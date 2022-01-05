
number=int(input())

def factorial(num):

    if num<=1:
        return 1
    else:
        return num*factorial(num-1)

print(factorial(number))

def factorial_for(number):
    result=1
    if number<=0:
        while number<0:
            print("0보다 작은 수 입니다 다시 입력해 주세요")
            number = int(input())
        if number>0:
            for i in range(1, number + 1):
                result *= i
        return print(result)
    else:
        for i in range(1, number + 1):
            result *= i
    return print(result)

factorial_for(number)

