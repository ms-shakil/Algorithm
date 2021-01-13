# linear search algorithm
array =[2,4,5,6,3,7,8,20]
seach_value = 5
def Linear_Search(arr,value):
    for i in range(len(arr)):
        if(arr[i]== value):
            return i
    return -1

print(Linear_Search(array,seach_value)   )            