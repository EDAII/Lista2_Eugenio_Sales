def bubble_sort(array):
    done = False
    while not done:
        done = True
        for i in range(len(array)-1):
            if array[i] > array[i+1]:
                array[i], array[i+1] = array[i+1], array[i]
                done  = False