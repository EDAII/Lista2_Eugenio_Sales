def selection_sort(array):

    for i in range(len(array)):
        index_min = i
        for j in range(i+i, len(array)):
            if array[j] < array[index_min]:
                index_min = j
        if index_min != i:
            array[i], array[index_min] = array[index_min], array[i]
