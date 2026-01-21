def selection_sort(arr) -> list:
    
    for i in range(len(arr)):
        k = i
        for j in range(i+1,len(arr)):
            if arr[j] < arr[k]:
                k = j
        temp = arr[i]
        arr[i] = arr[k]
        arr[k] = temp
    return arr
    
        