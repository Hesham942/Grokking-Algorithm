def quickSort(arr):
    if len(arr ) < 2:
        return arr
    else:
        pivot = arr[0]
        less = [i for i in arr[1:] if i <= pivot]
        greater = [j for j in arr[1:] if j > pivot]
        return quickSort(less) + [pivot] + quickSort(greater)
arr = [10, 5, 2, 3]
print(quickSort(arr))