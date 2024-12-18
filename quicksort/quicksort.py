def quicksort(arr): 
    if len(arr) < 2:
        return arr

    pivot = arr[len(arr)//2]
    left = [x for x in arr if x < pivot]
    mid = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]

    return quicksort(left) + mid + quicksort(right)



list = [49, 569, 1, 59, 12, 60, 5, 7]
result = quicksort(list)
print(f"Sorted Array {result}")