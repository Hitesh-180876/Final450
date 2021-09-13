

class Solution:
    def trappingWater(self, arr,n):
        
        left = [0]*n
        right = [0]*n
            
            
        water = 0
     
        left[0] = arr[0]
        for i in range( 1, n):
            left[i] = max(left[i-1], arr[i])
     
        right[n-1] = arr[n-1]
        for i in range(n-2, -1, -1):
            right[i] = max(right[i + 1], arr[i])
            
            
        for i in range(0, n):
            water += min(left[i], right[i]) - arr[i]
     
        return water
 
        #Code here

#{ 
#  Driver Code Starts
#Initial Template for Python 3

import math



def main():
        T=int(input())
        while(T>0):
            
            n=int(input())
            
            arr=[int(x) for x in input().strip().split()]
            obj = Solution()
            print(obj.trappingWater(arr,n))
            
            
            T-=1


if __name__ == "__main__":
    main()



# } Driver Code Ends
