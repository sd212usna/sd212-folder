# Search for a small gene pattern in a larger genetic sequence

# Read in the contents of dna.txt to a single large string
with open('dna.txt') as fin:
    dnaseq = fin.read().strip()

# This function finds the number of mismatches between
# the pattern and sequence at a single given position.
def mismatches(pattern, position):
    misses = 0
    for i in range(len(pattern)):
        if position + i >= len(dnaseq) or dnaseq[position + i] != pattern[i]:
            misses += 1
    return misses


# Get the search pattern from the terminal
pattern = input('enter search pattern: ')

# Get the best (smallest) number of mismatches
closest = len(pattern) # start with the most it could be, every character mismatches
for position in range(0, len(dnaseq)):
    mis = mismatches(pattern, position)
    if mis < closest:
        closest = mis

print(closest)
