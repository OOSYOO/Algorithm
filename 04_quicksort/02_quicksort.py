def quickSort(arr):
    if len(arr) < 2:
        return arr
    else:
        pivot = arr[0]

        less = [i for i in arr[1:] if i <= pivot] 
        grater = [i for i in arr[1:] if i > pivot]

        return quickSort(less) + [pivot] + quickSort(grater)

if __name__ == '__main__':
    arr = [2,5,3,1,77,5,44,5]
    print(quickSort(arr))
    
        