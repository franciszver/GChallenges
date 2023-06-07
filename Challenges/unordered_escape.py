# Fun fact: it took me a while to figure out how to phrase the "ask"
#     To my understanding, it's the following:
#         Given a 2 dimensional matrix of size w x h
#         That can have X number of states in each cell
    
#         How many starting original states can there be?
#             original = state that was not achieved by row/col swap manipulation of some other state
        
#     Given this, the logic should be that there would be some factorials involved since the nature of the solution is various states
#     After doing some research, it seems that matrixes manipulated this way can be simplified using Polya's Enumeration theorem
#     https://github.com/franklinvp/franklinvp.github.io/blob/master/_posts/2020-06-05-PolyaFooBar.md
#     The following code below is my attempt at coding this.

from collections import Counter

def buildGCDMatrix(m):
    # Build a matrix with a size less than max number
    
    # Initial size setup
    matrix = [[0 for x in range(m)] for y in range(m)]
    
    # Populate
    for i in range(m):
        for j in range(i, m):
            if i == 0 or j == 0:
                matrix[i][j] = 1
                matrix[j][i] = 1
            elif i == j:
                matrix[i][j] = i+1
            else:
                matrix[i][j] = matrix[i][j-i-1]
                matrix[j][i] = matrix[i][j-i-1]
    return matrix

def solution(w, h, s):
    # Determine the largest number
    m = 0
    if w > h:
        m = w
    else:
        m = h
    
    gcdmatrix = buildGCDMatrix(m)

    return str(gcdmatrix)


print(solution(2,2,2))
print(solution(2,3,4))