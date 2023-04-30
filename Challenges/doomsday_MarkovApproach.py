#New Pseudo code
# Note: This is my second attempt after trying my own solution forom before
# Note to myself: Watch patrickJMT's series on Markov Chains ep7-9
# thanks!: https://github.com/ivanseed/google-foobar-help/blob/master/challenges/doomsday_fuel/doomsday_fuel.md
# Approach is this... basically you identify the terminal arrays as the identity matrix because they go back to themselves
# List out the other arrays as non-absorbing
# so with the P = [I 0 R Q] which can be PMod = [I 0 FR 0]
# benefits with this problem is that you only need to pay attention to S0 after the PMod conversion


from fractions import Fraction
from fractions import gcd

t = [[0, 1, 0, 0, 0, 1], [4, 0, 0, 3, 2, 0], [0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0]]
ta = [0, 3, 2, 9, 14]
# t = [[0, 2, 1, 0, 0], [0, 0, 0, 3, 4], [0, 0, 0, 0, 0], [0, 0, 0, 0,0], [0, 0, 0, 0, 0]]

def lcm(a, b,):
  return a * b // gcd(a,b)

def findDenominator(a):
  aLen = len(a)
  if aLen <= 2:
    return lcm(*a)
  init = lcm(a[0], a[1])
  i = 2
  while i < aLen:
    init = lcm(init, a[i])
    i+=1
  return init

def convert(m):
  for j in range(len(m)):
    rowTotal = sum(m[j])
    if rowTotal == 0: # identify an absorbing state
      m[j][j] = 1 # add the one to indicate the identity matrix
    else:
      for k in range(len(m)):
        m[j][k] = Fraction(m[j][k], rowTotal) # adds probabilities

def subMatrix(matrix, rows, cols):
  tempMatrix = []
  for r in rows:
    currRow = []
    for c in cols:
      currRow.append(matrix[r][c])
    tempMatrix.append(currRow)
  return tempMatrix

def getQ(matrix, nonAbsorbingStates):
  return subMatrix(matrix, nonAbsorbingStates, nonAbsorbingStates)

def getR(matrix, nonAbsorbingStates, absorbingStates):
  return subMatrix(matrix, nonAbsorbingStates, absorbingStates)

def make2dList(n, m):
  a = []
  for r in range(n):
    a+=[[0]*m]
  return a

def makeIdentity(n):
  tempMatrix = make2dList(n,n)
  for j in range(n):
    tempMatrix[j][j] = 1
  return tempMatrix

def subtractMatrices(a, b):
  tempMatrix = []
  n, m = len(a), len(b)
  for j in range(n):
    r = []
    for k in range(m):
      r.append(a[j][k] - b[j][k])
    tempMatrix.append(r)
  return tempMatrix

def multiplyMatrices(a, b):
  ar, ac, bc = len(a), len(a[0]), len(b[0])
  c = make2dList(ar, bc)
  for j in range(ar):
    for k in range(bc):
      prod = Fraction(0,1)
      for l in range(ac):
        prod += a[j][l] * b[l][k]
      c[j][k] = prod
  return c

def addMultipleOfRowOfSqMatrix(matrix, sourceRow, k, targetRow):
  n = len(matrix)
  rowOp = makeIdentity(n)
  rowOp[targetRow][sourceRow] = k
  return multiplyMatrices(rowOp, matrix)

def multiplyRowOfSqMatrix(matrix, row, k):
  n = len(matrix)
  identity = makeIdentity(n)
  identity[row][row] = k
  return multiplyMatrices(identity, matrix)

def invertMatrix(matrix):
  n = len(matrix)
  inverse = makeIdentity(n)
  for col in range(n):
    diagonalRow = col
    k = Fraction(1, matrix[diagonalRow][col])
    matrix = multiplyRowOfSqMatrix(matrix, diagonalRow, k)
    inverse = multiplyRowOfSqMatrix(inverse, diagonalRow, k)
    sourceRow = diagonalRow
    for targetRow in range(n):
      if sourceRow != targetRow:
        k=-matrix[targetRow][col]
        matrix = addMultipleOfRowOfSqMatrix(matrix, sourceRow, k, targetRow)
        inverse = addMultipleOfRowOfSqMatrix(inverse, sourceRow, k, targetRow)
    return inverse

def solution(m):
  nonAbsorbingStates = []
  absorbingStates = []

  #First discover which states are absorbing and which are not
  for each in range(len(m)):
     if sum(m[each]) == 0:
        absorbingStates.append(each)
     else:
        nonAbsorbingStates.append(each)

  #Convert m to probabilities and provide the corresponding identity matrix
  convert(m)

  #Get q needed for the Markov calculations F = (I - Q)^-1
  q = getQ(m, nonAbsorbingStates)
  
  #Get r needed for the Markov calculations
  r = getR(m, nonAbsorbingStates, absorbingStates)

  # Make an identity matrix for use with the I section
  identity = makeIdentity(len(q))

  # (I - Q)
  diff = subtractMatrices(identity, q)

  # diff^-1
  inverse = invertMatrix(diff)

  result = multiplyMatrices(inverse, r)

  denominator = findDenominator([each.denominator for each in result[0]])
  result = [each.numerator * denominator // each.denominator for each in result[0]] # we just want the first of result because it's S0
  result.append(denominator)

  return result

print(solution(t))