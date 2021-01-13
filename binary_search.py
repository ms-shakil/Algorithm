# binary search by python
array =[1,3,5,6,8,9,10,15,18,19,20,21,22]
value = 20
def Binary_Search(array,value):
    left =0
    right =len(array)
    while left <= right:
        mid =(left+right)//2
        if array[mid] == value:
            return mid
        elif array[mid] < value :
            left =mid+1
        else:
            right= mid -1
    return -1               
print(Binary_Search(array,value))