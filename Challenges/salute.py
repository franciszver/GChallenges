testH = '>----<'

def solution(s):
    total = 0
    countR = 0
    for i in s:
        if i == '>':
            countR = countR + 1
        if i == '<':
            total = total + countR
    return total*2


print(solution(testH))