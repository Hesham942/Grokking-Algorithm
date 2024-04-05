def Binary_search(arr,item):
    low=0
    high=len(arr)-1

    while low<=high:
        mid = low + high // 2
        if arr[mid]==item:
            return mid
        if arr[mid]<item:
            low=mid+1
        else:
            high=mid-1
arr=[1,2,3,4,5,6,7,8,9,10]
print(Binary_search(arr,5))