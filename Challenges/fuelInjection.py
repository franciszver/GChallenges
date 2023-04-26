testInt = '3'
expected = 1

def solution(n):
    n = int(n)
    previous = 1
    total = 1
    steps = 0
    forwards = 0
    backwards = 0
    if n <= 2:
        return steps
    for i in range(n):
        if total == n:
            return steps
        if total > n:
            #check subtract
            backwards = 0
            for j in range(total*2):
                if total-j > n:
                    backwards = backwards + 1
                else:
                    break
            #check add
            forwards = 0
            for k in range(total*2):
                if previous+k < n:
                    forwards = forwards + 1
                else:
                    break
            if forwards == backwards:
                steps = steps + forwards-1
            if forwards < backwards:
                steps = steps + forwards-1
            if forwards > backwards:
                steps = steps + backwards
            return steps
        previous = total
        total = total * 2
        steps = steps + 1
    return steps

print(solution(testInt))