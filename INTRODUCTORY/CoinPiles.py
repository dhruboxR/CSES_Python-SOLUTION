def solve() : 
    left, right = map( int, input().split() )
    
    # small pile on the left 
    if right < left : 
        left, right = right , left
    
    if (left+right) % 3 == 0 and right <= 2 * left : 
        print( "YES" )
    else : print( "NO" )


testCase = int( input() )
for _ in range( testCase ) : 
    solve()

