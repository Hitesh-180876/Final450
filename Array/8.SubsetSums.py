class Solution:
    def subsetSums(self, arr, N):
        
        arr1=[]
        self.helper(arr,0,arr1,0)
        return arr1
        
    
    
    
    def helper(self,arr,curr_ind,arr1,summ):
        if(curr_ind>=len(arr)):
            arr1.append(summ)
            return
        self.helper(arr,curr_ind+1,arr1,summ+arr[curr_ind])
        self.helper(arr,curr_ind+1,arr1,summ)

        

#{ 
#  Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    T=int(input())
    for i in range(T):
        N = int(input())
        arr = [int(x) for x in input().split()]
        ob = Solution()
        ans = ob.subsetSums(arr, N)
        ans.sort()
        for x in ans:
            print(x,end=" ")
        print("")

# } Driver Code Ends
