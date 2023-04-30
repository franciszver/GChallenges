#New Pseudo code
#Get an array of terminals (if sum == 0, insert 1.  If sum>0 insert 0)
#For each entry, search M for references, and append the ratio in the position of array
#Check array of terminals, for 0 and S^0... if not all S^0, run check again
#IF passes check, simplifiy with same denominator
#steal numerators
#format reply, with numerators and TotalDenominator
from fractions import Fraction
from fractions import gcd


# t = [[0, 1, 0, 0, 0, 1], [4, 0, 0, 3, 2, 0], [0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0]]
# t = [[0, 2, 1, 0, 0], [0, 0, 0, 3, 4], [0, 0, 0, 0, 0], [0, 0, 0, 0,0], [0, 0, 0, 0, 0]]
t = [0]

def initializeAnswerArray(m):
    terminalIndexes = []
    for i in range(len(m)):
        if sum(list(m[i])) == 0:
            terminalIndexes.append([i, ['']]) #Using 0 to indicate start of calculation, and if remines 0, not valid termination path
        else:
            terminalIndexes.append([0, [-1]]) #Using -1 to indicate non-terminating position
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
                    probabilityFraction = Fraction(probability)
                    targetArray[each][0] = mTemp
                    targetArray[each][1].append(probabilityFraction)
                    break
    return targetArray

def checkIfDone(targetArray):
    for each in targetArray:
        if each[0] > 0:
            if len(each[1])>1:
                return 1
    return 0

#blatantly copied lcm code
def LCMofArray(a):
  lcm = a[0]
  for i in range(1,len(a)):
    lcm = lcm*a[i]//gcd(lcm, a[i])
  return lcm

def solution(m):
    if len(m) == 1:
        if len(m[0]) == 1 and m[0][0] == 0:
            return [1, 1]
    
    #Get an array of terminals (if sum == 0, insert 1, if sum>0 insert 0)
    #Example return arrayOfTerminals = [[0], [0], [1], [1], [1], [1]]
    keepGoing = 1
    arrayOfTerminals = (initializeAnswerArray(m))
    while keepGoing > 0:
        arrayOfTerminals = clean(m, arrayOfTerminals)
        keepGoing = checkIfDone(arrayOfTerminals)
    #for each entry, search M for references, and append the ratio in the position of array
    # arrayOfTerminals = appendProbabilities(m, arrayOfTerminals)
    answer = []
    denominators = []
    for cleanUpAnswer in arrayOfTerminals:
        if cleanUpAnswer[1][0] != -1:
            if cleanUpAnswer[1][0] == '':
                if len(cleanUpAnswer[1]) == 1:
                    answer.append(0)
                else:
                    #calculateTotalProbability
                    total = Fraction(1,1)
                    for fractions in cleanUpAnswer[1]:
                        if fractions != '':
                            total = total*fractions
                    denominators.append(total.denominator)
                    answer.append(total)
    commonDenominator = LCMofArray(denominators)
    for a in range(len(answer)):
        answer[a] = (answer[a]*commonDenominator).numerator
    finalSum = sum(answer)
    answer.append(finalSum)

    return answer
print(solution(t))