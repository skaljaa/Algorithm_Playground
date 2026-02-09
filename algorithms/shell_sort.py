def shell_sort(arr: list) -> list:
    n = len(arr)
    
    gap = n//2
    
    while gap > 0:
        for i in range(gap,n):
            current = arr[i]
            j = i
            while  j>= gap and arr[j-gap]>current:
                arr[j] = arr[j-gap]
                j -= gap
            arr[j] = current
            
        gap //= 2
        
    return arr