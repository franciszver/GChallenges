#this is the first step
test = ['aaaaa', 'abba', 'abccbaabccba', 'abcabcabcabc']
answers = [5, 1, 2, 4]

def solution(s):
    if len(s) % 2 == 1:
        #scenario 1: if all the same letters
        f = s[0]
        isSame = 1
        for i in s:
            if i != f:
                isSame = 0
        if isSame == 1:
            return len(s)
        else:
            return 1
    else:
        #scenario 2: palindrome approach
        halfindex = len(s)//2
        front_half = s[:halfindex]
        back_half = s[halfindex:]
        if front_half == back_half:
            return 2 * solution(front_half)
        else:
            return 1

for testies in test:
    print(solution(testies))