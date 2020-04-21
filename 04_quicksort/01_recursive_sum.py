def sum(arr):
    if len(arr) <= 1:
        return arr[0]
    return arr[0] + sum(arr[1:])

def lenArr(arr):
    if(len(arr) <=1 ):
        return 1

    return 1+lenArr(arr[1:])

def maxNum(arr):
    if(len(arr) <= 1):
        return arr[0]

    return max(arr[0], maxNum(arr[1:]))
    
if __name__ == "__main__":
    arr = [1,2,3,4,5]
    print(sum(arr))
    print(lenArr(arr))