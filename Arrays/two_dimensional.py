#day 1 - 11,15,10,6
#day 2 - 10,14,11,5
#day 3 - 12,17,12,8
#day 4 - 15,18,14,9

import numpy as np

twoDArray = np.array([[11,15,10,6], [10,14,11,5], [12,17,12,8], [15,18,14,9]])
print(twoDArray)


def searchTDArray(array, value): 
    for i in range(len(array)): #------------------> O(mn)
        for j in range(len(array[0])): #-----------> O(n)
            if array[i][j] == value: #-------------> O(1)
                return f'The value is located at index: {str(i)} {str(j)}' 
    return 'The element is not found' 

print(searchTDArray(twoDArray, 15))
