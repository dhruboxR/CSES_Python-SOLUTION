length = int( input() )
arr = list(map(int, input().split()))

increament = 0
for i in range(1, length) : 
    if arr[ i ] < arr[ i-1 ] : 
        increament += abs( arr[ i-1 ] - arr[ i ])
        arr[ i ] = arr[ i-1 ]

print( increament )