from itertools import permutations

string = input().strip()
string = sorted( string )

seenPermutations = set()

for perm in permutations( string ) :
    permString = "".join( perm )

    if permString not in seenPermutations :
        seenPermutations.add( permString )

seenPermutations = sorted( seenPermutations )

print( len(seenPermutations) )
for permutation in seenPermutations :
    print( permutation )