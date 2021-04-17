# insertion sort by python
lst = [1, 3, 4, 2, 5, 6, 9, 8, 7]


def Inserton_sort(lst):
    for i in range(1, len(lst), 1):
        item = lst[i]
        j = i-1
        while j >= 0 and lst[j] > item:
            lst[j+1] = lst[j]
            j -= 1
        lst[j+1] = item
    return lst


print(Inserton_sort(lst))
