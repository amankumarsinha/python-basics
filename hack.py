def countFreq(arr, n): 
  
    mp = dict() 
    pair=0
  
    # Traverse through array elements  
    # and count frequencies 
    for i in range(n): 
        if arr[i] in mp.keys(): 
            mp[arr[i]] += 1
        else: 
            mp[arr[i]] = 1
              
    # Traverse through map and print  
    # frequencies 
    for x in mp: 
        pair=pair+(int(mp[x]/2))
    print(pair)
  
# Driver code 
arr = [10, 20, 20, 10, 10, 20, 5, 20 ] 
n = len(arr) 
countFreq(arr, n) 
import numpy as np
a = np.random.rand(8,13,13)
