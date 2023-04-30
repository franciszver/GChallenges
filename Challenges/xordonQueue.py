start = 17
size = 4
expected = 14

start2 = 0
size2 = 3
expected2 = 2

# summary of problem is this pattern
# start with first number, xor those numbers until reach size difference
# skip to next start number, which is previousstart+iterationcount*startsize
# reduce workingsize by 1
# update previousstart to the new number, use the new number, keep xor until workingsize
# keep going until working size is 1
# then put out the xor number


def solution(start, length):
    
    return 0^1^2^3^4^6


print(solution(start, size), expected)
print(solution(start2, size2), expected2)