def selection_sort(arr):
    for i in range(len(arr)):
        min_index = i
        for j in range(i+1, len(arr)):
            if arr[j] < arr[min_index]:
                min_index = j
        arr[i], arr[min_index] = arr[min_index], arr[i]
    return arr


list = [49, 569, 1, 59, 12, 60, 5, 7]
result = selection_sort(list)
print(f"Sorted Array {result}")

