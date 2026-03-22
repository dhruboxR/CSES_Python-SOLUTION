def towerOfHanoi(numBlocks, sourceRod, destinationRod, helpingRod) :

    if numBlocks == 0 : return
    
    towerOfHanoi(numBlocks - 1, sourceRod, helpingRod, destinationRod)  # source -> helper
    
    print(sourceRod, destinationRod)

    towerOfHanoi(numBlocks - 1, helpingRod, destinationRod, sourceRod)  # helper -> destination

def solve() :
    numBlocks = int( input() )
    print((1 << numBlocks) - 1)       # minimum moves needed

    towerOfHanoi(numBlocks, 1, 3, 2)

testCase = 1 
for _ in range( testCase ) :
    solve()