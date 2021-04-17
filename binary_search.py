# binary search by python
def Binary_Search(array, value):
    left = 0
    right = len(array)
    while left <= right:
        mid = (left+right)//2
        if array[mid] == value:
            return mid
        elif array[mid] < value:
            left = mid+1
        else:
            right = mid - 1
    return -1


if __name__ == "__main__":
    array = [1, 3, 5, 6, 8, 9, 10, 15, 18, 19, 20, 21, 22]
    value = int(input("Enter a number:"))
    result = Binary_Search(array, value)
    if result == -1:
        if value in array:
            print(value, "is in list,but function returned -1")
        else:
            print(value, "not in list")

    else:
        if array[result] == value:
            print(value, "found in correct position.")
        else:
            print("Binary search returned", result,
                  "For", value, "which is incorrect.")
