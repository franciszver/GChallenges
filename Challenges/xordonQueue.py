start2 = 17
size2 = 4

start = 0
size = 3

start3 = 0
size3 = 42

# summary of problem is this pattern
# start with first number, xor those numbers until reach size difference
# skip to next start number, which is previousstart+iterationcount*startsize
# reduce workingsize by 1
# update previousstart to the new number, use the new number, keep xor until workingsize
# keep going until working size is 1
# then put out the xor number
# currently passes 1,2,3,7,8,10

# Update 2:
# idea is the efficiency of the logic fails with too many high iterations
# however, a quick internet search reveals that there's a pattern to iterative XOR operations at the binary level
# 


def f(a):
    res = (a, 1, a+1, 0)[a % 4]
    return res

def getXor(a, b):
    return f(b)^f(a-1)

def gen_nums(start, length):
    l = length
    ans = 0
    while l > 0:
        l = l-1
        ans^=getXor(start, start+l)
        start += length
    return ans

def solution(start, length):
    if length == 1:
        return start^(start+1)
    
    answer = start
    prevStart = start
    currNum = start+1
    iterations = 0
    totalIterations = length
    workingSize = length-1
    # keep going until working size is 0
    while totalIterations > 0:
        #start XORing until
        while workingSize > 0:
            answer = answer^currNum
            currNum += 1
            workingSize -= 1
        totalIterations -= 1
        #efficiency step
        checkForReduce = 1
        while checkForReduce > 0:
            if totalIterations%8 == 0 and totalIterations > 16:
                totalIterations = totalIterations/8
            else:
                checkForReduce = 0
                
        #prep next workload size
        workingSize = totalIterations
        iterations += 1
        prevStart = start+(iterations*length)
        currNum = prevStart
        # print('{0:08b}'.format(totalIterations), totalIterations, answer)
    return answer, gen_nums(start,length)


print(solution(start, size))
print(solution(start2, size2))
print(solution(start3, size3))