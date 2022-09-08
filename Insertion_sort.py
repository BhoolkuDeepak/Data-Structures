# Insertion Sort

def Naive_Insertion_sort(array):
    for i in range(1, len(array)):
        key = array[i]
        j = i-1
        while j >= 0 and array[j] > key:
            array[j+1] = array[j]
            j = j-1

        array[j+1] = key
    return array

a = [12, 20, 4, 5, 6, 4, 5, 2, 12]

print(Naive_Insertion_sort(a))
