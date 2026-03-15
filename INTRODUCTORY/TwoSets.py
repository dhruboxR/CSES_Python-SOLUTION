# division is only possible if sum till n is even
def solve() :
    n = int( input() )
    wholeSum = (n * (n + 1)) // 2

    if wholeSum & 1 :
        print( "NO" )
        return

    print( "YES" )
    target = wholeSum // 2

    first = set()
    second = set()

    firstSum = 0
    secondSum = 0
    temp = n

    # constructing the first set 
    while firstSum < target :
        rem = target - firstSum
        
        if rem < temp : 
            first.add( rem )
            break

        first.add( temp )
        firstSum += temp
        temp -= 1
    
    # constructing the second set 
    for i in range(1, n+1) :
        if secondSum >= target : break
        if i in first : continue 

        second.add( i )
        secondSum += i

    print( len(first) )
    print( *first )

    print( len(second) )
    print( *second )



testCase = 1
for _ in range( testCase ) : 
    solve()
