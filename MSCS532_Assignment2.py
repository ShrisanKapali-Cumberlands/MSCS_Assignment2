# Assignment 2
# Shrisan Kapali 005032249
# MSCS 532 Algorithms and Data Structure
# Implementation and comparision of divide-and-conquer algorithm

# imports
import time  # To calculate the run time
import random
import sys  # To calculate the size of static memory

# Implementation of merge sort
# A merge sort works by dividing recursively the data set into two half and sorting and merging the sublist


# Defining a recursive method to recursively divide the data sets into 2 halves using mid point
def merge_sort(array, left, right):
    # We call this method recursively only when the left < right
    if left < right:
        # Caclulating the mid point
        mid = (left + right) // 2

        # Now we recursively call this merge_sort method to partition left and right half
        # left is until the mid
        merge_sort(array, left, mid)
        # right is from mid+1 to right
        merge_sort(array, mid + 1, right)

        # Now after all we need to merge these sub list so
        merge(array, left, mid, right)


# A merge method
def merge(array, left, mid, right):
    # We create temporary sub arrays to get the left part and right part of the array
    left_temp_array = array[left : mid + 1]  # This is elements till mid
    right_temp_array = array[mid + 1 : right + 1]  # this is elements after mid to right

    # We need two pointers for subarrays
    i = j = 0
    # Pointer for main array
    k = left

    # Now merging the two temporary array
    while i < len(left_temp_array) and j < len(right_temp_array):
        if left_temp_array[i] <= right_temp_array[j]:
            array[k] = left_temp_array[i]
            i += 1
        else:
            array[k] = right_temp_array[j]
            j += 1
        k += 1

    # Now copying the remaing from left subarray
    while i < len(left_temp_array):
        array[k] = left_temp_array[i]
        i += 1
        k += 1

    # Now copying the remaing from right subarray
    while j < len(right_temp_array):
        array[k] = right_temp_array[j]
        j += 1
        k += 1
