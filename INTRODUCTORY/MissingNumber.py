# Read length and the array 
n = int( input() )
arr = list( map(int, input().split() ) )

# missing number = total sum till n - total sum of arr 
arrSum = sum( arr )
totSum = (n * (n+1)) // 2;

missingNumber = totSum - arrSum
print( missingNumber )

