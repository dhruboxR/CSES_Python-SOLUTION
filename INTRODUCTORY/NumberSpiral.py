def solve() :
    row , column = map(int, input().split() )

    if row <= column :
        if(column&1) :
            print( column*column - (row-1) )
        else : print( (column-1)*(column-1) + row)
    else :
        if(row&1) :
            print( (row-1)*(row-1) + column )
        else : print( row *  row - (column-1) )

testCase = int( input() )
for _ in range( testCase ) :
    solve()
