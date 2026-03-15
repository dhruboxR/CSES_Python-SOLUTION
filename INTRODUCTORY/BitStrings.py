# For every position, 2 options : put a 1 / put a 0
# For n positions we get 2^n strings in total 

def solve() : 
    mod = 1000000007
    n = int( input() )

    print( pow(2, n, mod) )

testCase = 1
for _ in range( testCase ) : solve()
