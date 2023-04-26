def solution(n):
    n = int(n)
    steps = 0
    if n == 1:
        return 0
    while n > 1:
        print(n)
        if n%2 == 0:
            steps = steps+1
            n = n/2
        else:
            #test up and down
            if ((n-1)/2) == 1:
                steps = steps + 1
                n = n-1
            if ((n-1)/2)%2 == 0:
                steps = steps + 1
                n = n-1
            else:
                steps = steps + 1
                n = n+1
    return steps
    

for i in range(100):
    print(solution(i), i)