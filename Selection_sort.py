# SELECTION SORT
def Naive_selection_sort(array):
    new = []
    for i in range (len(a)):
        min_id=0
        for j in range(len(a)):
            if a[j] < a[min_id]:
                min_id=j
        new.append(a[min_id])
        a.pop(min_id)
    return(new)

#Naive selection sort creates a new table and appends the values 
#regular selection sort swaps the values with the current outer iterator with the minimum value 

def Selection_sort(array):
    for i in range (len(array)):
        min_id=i
        j=i+1
        while j in range(len(array)):
            if array[j]<array[min_id]:
                min_id=j
            j=j+1
        array[min_id],array[i]=array[i],array[min_id]

    return (array)    

a = [10, 5,8,20,2,8,8,8,8]

print(Selection_sort(a))
print(Naive_selection_sort(a))