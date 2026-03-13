n = int( input() )
sequence = []

while n != 1 : 
    sequence.append( n )

    if n%2 == 0 : 
        n = n // 2
    else : 
        n = 3 * n + 1

sequence.append( 1 )
print( *sequence )

# Implementation : 1 

        # n = int( input() )

        # while True : 
        #     print(n, end = " ")

        #     if( n == 1 ) : break

        #     if( n%2 == 0 ) : 
        #         n = n // 2
        #     else :
        #         n = 3 * n + 1

# Implementation : 2

        # def collatz( n ) : 
        #     while n != 1 :
        #         print(n, end = " ")

        #         if n%2 == 0 : 
        #             n = n // 2
        #         else :
        #             n = 3 * n + 1

        # n = int( input() )
        # collatz( n )

# Implementation : 3
