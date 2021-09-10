
class Solution:
    def sort012(self,arr,n):
        zeroes = 0
        ones = 0
        twos = 0
        # code here
        for i in range(n):
            if arr[i] == 0:
                zeroes+=1
            elif arr[i] == 1:
                ones+=1
            elif arr[i] == 2:
                twos+=1
        
        i = 0
        while zeroes>0:
            arr[i] = 0
            i+=1
            zeroes-=1
            
        
        while ones>0:
            arr[i] = 1
            i+=1
            ones-=1
            
        while twos>0:
            arr[i] = 2
            i+=1
            twos-=1
        return arr
        

#{ 
#  Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    t=int(input())
    for _ in range(t):
        n=int(input())
        arr=[int(x) for x in input().strip().split()]
        ob=Solution()
        ob.sort012(arr,n)
        for i in arr:
            print(i, end=' ')
        print()

# } Driver Code Ends
