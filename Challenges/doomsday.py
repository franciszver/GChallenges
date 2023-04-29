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
            terminalIndexes.append([i, 1]) #Using -1 to indicate start of calculation
        else:
            terminalIndexes.append([0, -1]) #Using -1 to indicate non-terminating position
    return terminalIndexes

def clean(m, targetArray):
    for each in range(len(targetArray)):
        if targetArray[each][0] != 0:
            #searchMarrayForReferenceToThatTarget, store position and multiply probability
            for mTemp in range(len(m)):
                mTempArray = m[mTemp]
                if mTempArray[each] > 0:
                    print(mTempArray)
                    total = sum(list(mTempArray))
                    print(total)
                    print(mTempArray[each])
                    probability = str(mTempArray[each]) + '/' + str(total)
                    print(probability)
                    targetArray[each][0] = mTemp
                    targetArray[each][1] = probability
                    print(targetArray[each])
                    break
    return targetArray

def solution(m):
    #Get an array of terminals (if sum == 0, insert 1, if sum>0 insert 0)
    #Example return arrayOfTerminals = [[0], [0], [1], [1], [1], [1]]
    arrayOfTerminals = (initializeAnswerArray(m))
    print(arrayOfTerminals)
    arrayOfTerminals = clean(m, arrayOfTerminals)
    #for each entry, search M for references, and append the ratio in the position of array
    # arrayOfTerminals = appendProbabilities(m, arrayOfTerminals)
    
    return arrayOfTerminals


print(solution(t))