def shell_sort(array):

    h = 1
    while h > 0:
            for i in range(h, len(array)):
                c = array[i]
                j = i
                while j >= h and c < array[j - h]:
                    array[j] = array[j - h]
                    j = j - h
                    array[j] = c
            h = int(h / 2.2)