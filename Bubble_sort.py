# BUBBLE SORT

def Bubble_sort(array):
    l = 0
    k = len(array)
    while l < k-1:
        for i in range(len(array)-l-1):
            j = i+1
            while array[i] > array[j]:
                array[i],array[j] = array[j],array[i]
        l = l+1
    return(array)

a = [11, 2, 3, 5, 6, 7, 8, 9, 4]

print(Bubble_sort(a))