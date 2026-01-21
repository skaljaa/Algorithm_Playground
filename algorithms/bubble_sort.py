def bubble_sort(arr):  
    for i in range(len(arr)):
        swapped = False
        for j in range(len(arr)-1-i):
            if arr[j]>arr[j+1]:
                swapped = True
                temp = arr[j]
                arr[j] = arr[j+1]
                arr[j+1] = temp
        if not swapped:
            return arr
    return arr