#determine the terminal possibilities, these are the arrays with 0 numbers (sum is 0)
#determine the possibilities to get to them, evaluate each terminal possibility
#sum all possibilities = denominator
#return posibilities for each terminal + denominator

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