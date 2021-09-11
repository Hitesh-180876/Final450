import sys
class Solution:
    ##Complete this function
    #Function to find the sum of contiguous subarray with maximum sum.
    def maxSubArraySum(self,arr,N):
        
        maxSum = -sys.maxsize
        currSum = 0
        
        for i in range(N):
            currSum = currSum+arr[i]
            
            if maxSum<currSum:
                maxSum = currSum
            
            if currSum<0:
                currSum = 0
            
        return maxSum
            
        
        ##Your code here

#{ 
#  Driver Code Starts
#Initial Template for Python 3

import math

 
def main():
        T=int(input())
        while(T>0):
            
            n=int(input())
            
            arr=[int(x) for x in input().strip().split()]
            
            ob=Solution()
            
            print(ob.maxSubArraySum(arr,n))
            
            T-=1


if __name__ == "__main__":
    main()
# } Driver Code Ends
