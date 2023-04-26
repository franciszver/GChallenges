def solution(n):
    n = int(n)
    previous = 1
    total = 1
    steps = 0
    forwards = 0
    backwards = 0
    if n == 1:
        print('1st attempt')
        return steps
    while n >= 1:
        if n%2 == 0:
            steps = steps + 1
            n = n/2
        if n%2 != 0:
            steps = steps+1
            n = n-1
    print('2nd attempt')
    return steps-1


for i in range(100):
    print(solution(i), i)