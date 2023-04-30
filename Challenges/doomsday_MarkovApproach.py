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



def applyProbability(m):
  for r in range(len(m)):
    total = 0
    for each in range(len(m[r])):
      total += m[r][each]
    if total != 0:
      for each in range(len(m[r])):
        m[r][each] /= float(total)
  return m

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