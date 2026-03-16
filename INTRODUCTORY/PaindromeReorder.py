def solve() :
    string = input()
    
    charFreq = {}                       # Dictionary to stroe the key-value pair 
    for character in string :
        charFreq[ character ] = charFreq.get(character, 0) + 1

    # construct the palindromic string 
    ends = ""   # frontend = ends , backend = reverse of ends
    mid = ""

    for character in charFreq :
        # odd frequency element
        if charFreq[ character ] & 1 :
            if mid != "" : 
                print( "NO SOLUTION" )
                return
            mid = character * charFreq[ character ]   # single character , freq number of times
        else :
            ends += character * (charFreq[ character ] // 2) 
    
    print(ends + mid + ends[ ::-1 ])

solve()