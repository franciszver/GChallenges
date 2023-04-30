#New Pseudo code
# Note: This is my second attempt after trying my own solution forom before
# Note to myself: Watch patrickJMT's series on Markov Chains ep7-9
# thanks!: https://github.com/ivanseed/google-foobar-help/blob/master/challenges/doomsday_fuel/doomsday_fuel.md
# Approach is this... basically you identify the terminal arrays as the identity matrix because they go back to themselves
# List out the other arrays as non-absorbing
# so with the P = [I | 0 / R | Q] which can be PMod = [I | 0 / FR | 0]
# benefits with this problem is that you only need to pay attention to S0 after the PMod conversion
# and help by algomaster99 as well

t = [[0, 1, 0, 0, 0, 1], [4, 0, 0, 3, 2, 0], [0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0]]
ta = [0, 3, 2, 9, 14]
# t = [[0, 2, 1, 0, 0], [0, 0, 0, 3, 4], [0, 0, 0, 0, 0], [0, 0, 0, 0,0], [0, 0, 0, 0, 0]]

from fractions import Fraction
from fractions import gcd

def rqCalc(m, absorbingStates, nonAbsorbingStates):
  r = []
  q = []
  for i in nonAbsorbingStates:
    tempT = []
    tempN = []
    for j in absorbingStates:
      tempT.append(m[i][j])
    for j in nonAbsorbingStates:
      tempN.append(m[i][j])
    r.append(tempT)
    q.append(tempN)
  return r, q

def subtractIQ(q):
  n = len(q)
  for r in range(len(q)):
    for each in range(len(q[r])):
      if r == each:
        q[r][each] = 1 - q[r][each]
      else:
        q[r][each] = -q[r][each]
  return q

def getDeterminant(q): #assuming q is a square matrix
  #quick returns
  if len(q) == 1:
    return q[0][0]
  if len(q) == 2:
    return q[0][0]*q[1][1] - q[0][1] * q[1][0]

  determinant = 0
  for firstRofEach in range(len(q[0])):
    subMatrix = getSubMatrix(q, 0, firstRofEach)
    determinant += (((-1)**firstRofEach)*q[0][firstRofEach] * getDeterminant(subMatrix))
  
  return determinant

def getConvertedSqMatrix(q):
  for i in range(len(q)):
    for j in range(i, len(q), 1):
      q[i][j], q[j][i] = q[j][i], q[i][j]
  return q

def productMatrix(a, b):
  result = []
  temp = len(a)
  for r in range(len(a)):
    tempArray = []
    for col in range(len(b[0])):
      product = 0
      for sel in range(temp):
        product += (a[r][sel]*b[sel][col])
      tempArray.append(product)
    result.append(tempArray)
  return result

def applyProbability(m):
  for r in range(len(m)):
    total = 0
    for each in range(len(m[r])):
      total += m[r][each]
    if total != 0:
      for each in range(len(m[r])):
        m[r][each] /= float(total)
  return m

def getSubMatrix(q, i, j):
  subMatrix = []
  for r in q[:i] + q[i+1:]:
    temp = []
    for each in r[:j] + r[j+1:]:
      temp.append(each)
    subMatrix.append(temp)
  return subMatrix

def getInverse(q):
  q1 = []
  for r in range(len(q)):
    temp = []
    for col in range(len(q[r])):
      subMatrix = getSubMatrix(q, r, col)
      determinant = getDeterminant(subMatrix)
      temp.append(((-1)**(r+col))*determinant)
    q1.append(temp)
  mainDeterminant = getDeterminant(q)
  q1 = getConvertedSqMatrix(q1)


def cleanup(m):
  # Basically convert the fractions into a/b form so that the denominator can be determined and reported on
  s0 = m[0]
  toFraction = [Fraction(i).limit_denominator() for i in s0]
  lcm = 1
  for i in toFraction:
    if i.denominator != 1:
      lcm = i.denominator
  for i in toFraction:
    if i.denominator != 1:
      lcm = lcm*i.denominator/gcd(lcm, i.denominator)
  toFraction = [(i*lcm).numerator for i in toFraction]
  toFraction.append(lcm)
  for each in range(len(toFraction)):
    toFraction[each] = int(toFraction[each])
  return toFraction

def solution(m):
  n = len(m)

  #address the unique case of just 1 state
  if n==1:
     if len(m[0]) ==1 and m[0][0] == 0:
        return [1,1]
  
  absorbingStates = []
  nonAbsorbingStates = []

  #First discover which states are absorbing and which are not
  for r in range(len(m)):
    count = 0
    for each in range(len(m[r])):
      if m[r][each] == 0:
        count += 1
    if count == n:
      absorbingStates.append(r)
    else:
      nonAbsorbingStates.append(r)

  #apply probabilities in the rows, crucial for nonAbsorbingStates
  probabilities = applyProbability(m)

  # get R and Q and handle the (I - Q) part of F=(I-Q)^1
  r, q = rqCalc(probabilities, absorbingStates, nonAbsorbingStates)

  #now get an identity matrix to use
  iq = subtractIQ(q)

  #Get the F by inversing and finishing
  inverseF = getInverse(iq)
  fr = productMatrix(inverseF, r)
  
  #now matrix manipulation needed to create an answer acceptable by GOOGLE
  return cleanup(fr)


print(solution(t))