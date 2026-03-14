# total positions - number of attacking positions 

drange = int( input() )

for i in range (1, drange+1) :
    tpos = i * i

    if i == 1 :
        print( 0 )
    else :
        total = (tpos * (tpos-1)) // 2
        # number of 2*3 slabs in the grid : each slab got 2 attacking positions
        attack_pos = 2 * (i -1) * (i - 2)
        # number of 3*2 slabs in the grid : each slab got 2 attacking positions
        attack_pos += 2 * (i - 1) * (i - 2)

        print( total - attack_pos )

