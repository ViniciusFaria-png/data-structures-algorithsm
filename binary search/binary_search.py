def bs(arr, target):
    low, high = 0, len(arr)-1
    mid = (low + high) // 2
    clue = arr[mid]
    while low <= high:
        if target == clue:
            return mid
        if target > clue:
            low = mid + 1
        else:
            high = mid - 1
    return None


list = [1,2,3,4,5,6,7,8,9,10]
target = 5
result = bs(list, target)


if result == None:
    print(f"Valor {target} nao encontrado")
else:
    print(f"Valor {target} encontrado na posicaçao {result} ")

