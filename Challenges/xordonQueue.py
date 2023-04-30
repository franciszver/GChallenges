start2 = 17
size2 = 4
expected2 = 14

start = 0
size = 3
expected = 2

# summary of problem is this pattern
# start with first number, xor those numbers until reach size difference
# skip to next start number, which is previousstart+iterationcount*startsize
# reduce workingsize by 1
# update previousstart to the new number, use the new number, keep xor until workingsize
# keep going until working size is 1
# then put out the xor number


def solution(start, length):
    answer = start
    prevStart = start
    currNum = start
    iterations = 0
    totalIterations = length
    workingSize = length
    # keep going until working size is 0
    while totalIterations > 0:
        #start XORing until
        currNum = prevStart
        usedArray = []
        while workingSize > 0:
            usedArray.append(currNum)
            answer = answer^currNum
            currNum += 1
            workingSize -= 1
        totalIterations -= 1
        #prep next workload size
        workingSize = totalIterations
        iterations += 1
        prevStart = start+(iterations*length)
        print('usedArray', usedArray)
    
    return answer


print(solution(start, size))
print(solution(start2, size2))