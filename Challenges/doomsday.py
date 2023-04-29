#New Pseudo code
#Get an array of terminals (if sum == 0, insert 1.  If sum>0 insert 0)
#For each entry, search M for references, and append the ratio in the position of array
#Check array of terminals, for 0 and S^0... if not all S^0, run check again
#IF passes check, simplifiy with same denominator
#steal numerators
#format reply, with numerators and TotalDenominator

t = [[0, 1, 0, 0, 0, 1], [4, 0, 0, 3, 2, 0], [0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0]]

def solution(m):
    arrOfTerminals = (returnListOfTerminals(m))
    return arrOfTerminals

def returnListOfTerminals(m):
    terminalIndexes = []
    searchIndex = 0
    for i in m:
        if sum(list(i)) == 0:
            terminalIndexes.append(searchIndex)
        searchIndex = searchIndex + 1
    return terminalIndexes

print(solution(t))