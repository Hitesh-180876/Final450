def rearrange(arr, n):
    
    j = 0
    for i in range(0, n):
        if arr[i]<0:
            arr[i],arr[j] = arr[j],arr[i]
            
            j = j+1
    
    print(arr)
n = 5
arr = [-1, 3, 5, -2, -6]
rearrange(arr, n)
