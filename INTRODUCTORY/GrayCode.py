def solve() :
    n = int( input() )
    string = '0' * n
    
    codes = []
    codes.append( string )

    cnt = 1
    limit = 1 << n
    bitPos = n - 1

    while cnt < limit :
        # insertion from bottom to top 
        for i in range( len(codes)-1, -1, -1 ) :
            
            newCode = list( codes[ i ] )        # convert string to list 
            newCode[ bitPos ] = '1'             # modify the bit


            codes.append( ''.join( newCode ) )  # convert back to string 
            cnt += 1
        
        bitPos -= 1
    
    for code in codes :
        print( code )

testCase = 1
for _ in range( testCase ) :
    solve()

# In Python, strings are immutable, so you cannot assign to an index like newCode[bitPos] = '1'