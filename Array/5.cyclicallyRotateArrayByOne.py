
def rotate( arr, n):
    
    temp = arr[n-1]
    
    i = 1
    while n>i:
        arr[n-i] = arr[n-1-i]
        i = i+1
    arr[0] = temp
    return arr    
    
    


#{ 
#  Driver Code Starts
#Initial Template for Python 3

def main():

    T = int(input())

    while(T > 0):
        n = int(input())
        a = [int(x) for x in input().strip().split()]
        rotate(a, n)
        print(*a)

        T -= 1


if __name__ == "__main__":
    main()





    
# } Driver Code Ends
