# check all possible combinations of groups 
def appleDivision(weights, idx, goneSum, gtwoSum) :
    if(idx == len( weights) ) :
        return abs(goneSum - gtwoSum)
    
    # include the element in the first group 
    firstSum = appleDivision(weights, idx+1, goneSum+weights[ idx ], gtwoSum)

    # include the element in the secon group
    secondSum = appleDivision(weights, idx+1, goneSum, gtwoSum+weights[ idx ])

    return min(firstSum, secondSum)

def solve() :
    length = int( input() )
    weights = list( map(int, input().split()) )

    diff = appleDivision(weights, 0, 0, 0)
    
    print( diff )

testCase = 1
for _ in range( testCase ) :
    solve()
