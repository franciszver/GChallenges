#New Pseudo code
#Get an array of terminals (if sum == 0, insert 1.  If sum>0 insert 0)
#For each entry, search M for references, and append the ratio in the position of array
#Check array of terminals, for 0 and S^0... if not all S^0, run check again
#IF passes check, simplifiy with same denominator
#steal numerators
#format reply, with numerators and TotalDenominator

t = [[0, 1, 0, 0, 0, 1], [4, 0, 0, 3, 2, 0], [0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0]]

def initializeAnswerArray(m):
    terminalIndexes = []
    for i in range(len(m)):
        if sum(list(m[i])) == 0:
            terminalIndexes.append([i, '']) #Using 0 to indicate start of calculation, and if remines 0, not valid termination path
        else:
            terminalIndexes.append([0, -1]) #Using -1 to indicate non-terminating position
    return terminalIndexes

def clean(m, targetArray):
    for each in range(len(targetArray)):
        if targetArray[each][0] != 0:
            #searchMarrayForReferenceToThatTarget, store position and multiply probability
            for mTemp in range(len(m)):
                mTempArray = m[mTemp]
                if mTempArray[targetArray[each][0]] > 0:
                    total = sum(list(mTempArray))
                    probability = str(mTempArray[targetArray[each][0]]) + '/' + str(total)
                    targetArray[each][0] = mTemp
                    targetArray[each][1] = str(targetArray[each][1]) + '.' + probability
                    break
    return targetArray

def checkIfDone(targetArray):
    for each in targetArray:
        if each[0] > 0:
            if len(each[1])>1:
                return 1
    return 0

def solution(m):
    #Get an array of terminals (if sum == 0, insert 1, if sum>0 insert 0)
    #Example return arrayOfTerminals = [[0], [0], [1], [1], [1], [1]]
    keepGoing = 1
    arrayOfTerminals = (initializeAnswerArray(m))
    while keepGoing > 0:
        arrayOfTerminals = clean(m, arrayOfTerminals)
        keepGoing = checkIfDone(arrayOfTerminals)
    #for each entry, search M for references, and append the ratio in the position of array
    # arrayOfTerminals = appendProbabilities(m, arrayOfTerminals)
    return arrayOfTerminals


print(solution(t))