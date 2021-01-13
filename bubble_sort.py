# bubble sort by python
array=[5,7,4,3,8,5,9,43,46,75,54,756,54]
def Bubble_sort(arr):
    for i in range(len(arr)):
        for j in range(len(arr)-i-1):
            if(arr[j]>arr[j+1]):
                T = arr[j]
                arr[j] = arr[j+1]
                arr[j+1] = T
    return  arr

print(Bubble_sort(array))    
