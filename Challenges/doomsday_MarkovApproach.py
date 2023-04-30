#New Pseudo code
# Note: This is my second attempt after trying my own solution forom before
# Note to myself: Watch patrickJMT's series on Markov Chains ep7-9
# thanks!: https://github.com/ivanseed/google-foobar-help/blob/master/challenges/doomsday_fuel/doomsday_fuel.md
# Approach is this... basically you identify the terminal arrays as the identity matrix because they go back to themselves
# List out the other arrays as non-absorbing
# so with the P = [I 0 R Q] which can be PMod = [I 0 FR 0]
# benefits with this problem is that you only need to pay attention to S0 after the PMod conversion
# and help by algomaster99 as well

t = [[0, 1, 0, 0, 0, 1], [4, 0, 0, 3, 2, 0], [0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0]]
ta = [0, 3, 2, 9, 14]
# t = [[0, 2, 1, 0, 0], [0, 0, 0, 3, 4], [0, 0, 0, 0, 0], [0, 0, 0, 0,0], [0, 0, 0, 0, 0]]


from fractions import Fraction

def solution(m):
  n = len(m)
  if n==1:
     if len(m[0]) ==1 and m[0][0] == 0:
        return [1,1]
  
  absorbing_states = []
  nonAbsorbingStates = []

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