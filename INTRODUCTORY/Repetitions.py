def longest_sequence( word ) : 
    current_len = 1
    max_len = 1

    for i in range(1, len(word)) :
        if(word[ i ] == word[ i-1 ]) : current_len += 1
        else :
            max_len = max(current_len, max_len)
            current_len = 1
    
    max_len = max(current_len, max_len)
    print( max_len )

word = input().strip()
longest_sequence( word )