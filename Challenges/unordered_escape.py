# Fun fact: it took me a while to figure out how to phrase the "ask"
#     To my understanding, it's the following:
#         Given a 2 dimensional matrix of size w x h
#         That can have X number of states in each cell
#         How many starting original states can there be?
#             original = state that was not achieved by row/col swap manipulation of some other state
#     Given this, the logic should be that there would be some factorials involved since the nature of the solution is various states
#     After doing some research, it seems that matrixes manipulated this way can be simplified using Polya's Enumeration theorem
#     This theorem provides a way to graph and calculate arrangements, and can be used to discover the number of arrangements
#       given the current matrix question, and then needs to be modified to remove the possibilities that represent "Equivalency"
#     https://github.com/franklinvp/franklinvp.github.io/blob/master/_posts/2020-06-05-PolyaFooBar.md
#     https://en.wikipedia.org/wiki/P%C3%B3lya_enumeration_theorem
#     The following code below is my attempt at coding this with guidance from a friend.

from collections import Counter


def preCalcFactorial(x, factorialMatrix):
    # Returns the intended pre calculated factorial
    return factorialMatrix[x-1]


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

def buildFactorialMatrix(m):
    # this is gonna be big, but it'll save time end effort later, build the factorials of all the numbers until max

    matrix = [1]
    for i in range(m-1):
        matrix.append(matrix[-1]*(i+2))
    return matrix

def coefFact(pt, m, factorialMatrix):
    # Calculate coefficient factorials based on the algo integrating the theorem
    cf = preCalcFactorial(m, factorialMatrix)
    for a, b in Counter(pt).items():
        cf=cf/((a**b)*preCalcFactorial(b, factorialMatrix))
    return cf

def preCalcGCD(x, y, gcdMatrix):
    return gcdMatrix[x-1][y-1]

def partitionsCycles(m, factorialMatrix):
    # Cycling through and computing the count through part of the forumla provided in the Polya's enumeration theorem
    # The algorithm used is from the following: https://arxiv.org/pdf/0909.2331.pdf

    matrix = []
    q = m*[0]
    q[0] = m
    a = [0 for i in range(m+1)]
    l = 1
    z = m-1
    while l != 0:
        y = a[l-1]+1
        l = l-1
        while 2 * y <= z:
            a[l] = y
            z = z-y
            l = l+1
        mm = l+1
        while y <= z:
            a[l] = y
            a[mm] = z
            part = a[:l+2]
            matrix.append((part, coefFact(part, m, factorialMatrix)))
            y = y+1
            z = z-1
        a[l] = y+z
        z = y+z-1
        part = a[:l+1]
        matrix.append((part, coefFact(part, m, factorialMatrix)))
    return matrix

def solution(w, h, s):
    # Determine the largest number
    m = 0
    if w > h:
        m = w
    else:
        m = h

    # and get the greatest common denominator for them in a matrix
    gcdmatrix = buildGCDMatrix(m)

    # precalculate the factorials to save us time
    factorialMatrix = buildFactorialMatrix(m)

    # Now breaking it down to partitions as implemented in the Polya's enumeration theorem
    result = 0
    for cw in partitionsCycles(w, factorialMatrix):
        for ch in partitionsCycles(h, factorialMatrix):
            o = cw[1]*ch[1]
            result=result+(o*(s**sum([sum([preCalcGCD(i, j, gcdmatrix) for i in cw[0]]) for j in ch[0]])))
    return str(result/(preCalcFactorial(w, factorialMatrix)*preCalcFactorial(h, factorialMatrix)))



print('answer ', solution(2,2,2))
print('answer ', solution(2,3,4))