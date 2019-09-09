from ordenation_methods.insertion_sort import insertion_sort
from ordenation_methods.bubble_sort import bubble_sort
from ordenation_methods.shell_sort import shell_sort
from ordenation_methods.selection_sort import selection_sort
from random import randint
import time


def switch_method(method, max):

    array = []
    for i in range (0, max+1):
        array.append(randint(0, max+1))

    if method == 'Insertion':
        begin = time.time()
        insertion_sort(array)
        end = time.time()
        return (end - begin)

    elif method == 'Selection':
        begin = time.time()
        selection_sort(array)
        end = time.time()
        return (end - begin)
    
    elif method == 'Shell':
        begin = time.time()
        shell_sort(array)
        end = time.time()
        return (end - begin)
    
    elif method == 'Bubble':
        begin = time.time()
        bubble_sort(array)
        end = time.time()
        return (end - begin)
