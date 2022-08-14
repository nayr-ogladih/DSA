#day 1 - 11,15,10,6
#day 2 - 10,14,11,5
#day 3 - 12,17,12,8
#day 4 - 15,18,14,9

import numpy as np

twoDArray = np.array([[11,15,10,6], [10,14,11,5], [12,17,12,8], [15,18,14,9]])
print(twoDArray)

newTDArray = np.delete(twoDArray, 3, axis=0)
print(newTDArray)


#O(mn)
#space complexity: O(1)