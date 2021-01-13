# selection sort by python
array=[5,7,4,3,8,5,9,43,46,75,54,756,54]
def Selection_Sort(arr):
    for i in range(len(arr)):
        dd = i
        for j in range(i+1,len(arr),1):
            if arr[j] < arr[i]:
                dd = j
        if dd != i:
            T = arr[i]
            arr[i]= arr[dd]
            arr[dd]= T    
    print(arr)            
Selection_Sort(array)    