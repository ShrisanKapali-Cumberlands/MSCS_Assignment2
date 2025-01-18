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


# Use cases with different array lists
sortedArray = list(range(0, 500))  # Sorted array from 1 to 499
reverseSortedArray = list(range(500, 0, -1))  # Reverse sorted array from 499 to 1
randomSortedArray = [
    random.randint(1, 500) for _ in range(500)
]  # Random array of size 500


# Applying merge sort in the above arrays
print("")
print("*************** Merge Sort Implementation **************")
print("")
print("Applying merge sort to array 1 which is sorted")
startTime = time.time()
merge_sort(sortedArray, 0, len(sortedArray) - 1)
endTime = time.time()
print("Start time for sort process", startTime)
print("End time for sort process", endTime)
print(f"Execution time: {endTime - startTime:.6f} seconds")
originalMemorySize = sys.getsizeof(sortedArray)
additionalMemorySize = sys.getsizeof(merge_sort(sortedArray, 0, len(sortedArray) - 1))
totalMemorySize = originalMemorySize + additionalMemorySize
print("Original memory size", originalMemorySize)
print("Additional memory used", additionalMemorySize)
print("Total memory used", totalMemorySize)
print("sortedArray", sortedArray)


print("")
print("Applying merge sort to array 2 which is reverse sorted")
startTime = time.time()
merge_sort(reverseSortedArray, 0, len(reverseSortedArray) - 1)
endTime = time.time()
print("Start time for sort process", startTime)
print("End time for sort process", endTime)
print(f"Execution time: {endTime - startTime:.6f} seconds")
originalMemorySize = sys.getsizeof(reverseSortedArray)
additionalMemorySize = sys.getsizeof(
    merge_sort(reverseSortedArray, 0, len(reverseSortedArray) - 1)
)
totalMemorySize = originalMemorySize + additionalMemorySize
print("Original memory size", originalMemorySize)
print("Additional memory used", additionalMemorySize)
print("Total memory used", totalMemorySize)
print("sortedArray", reverseSortedArray)

print("")
print("Applying merge sort to array 3 which is random sorted")
startTime = time.time()
merge_sort(randomSortedArray, 0, len(randomSortedArray) - 1)
endTime = time.time()
print("Start time for sort process", startTime)
print("End time for sort process", endTime)
print(f"Execution time: {endTime - startTime:.6f} seconds")
originalMemorySize = sys.getsizeof(randomSortedArray)
additionalMemorySize = sys.getsizeof(
    merge_sort(randomSortedArray, 0, len(randomSortedArray) - 1)
)
totalMemorySize = originalMemorySize + additionalMemorySize
print("Original memory size", originalMemorySize)
print("Additional memory used", additionalMemorySize)
print("Total memory used", totalMemorySize)
print("sortedArray", randomSortedArray)


########### Quick Sort implementation #############
########### Quick Sort implementation using right most element as pivot #############
## Creating a method to implment quick sort
def quick_sort_using_righmost_element(array, low, high):
    if low < high:
        pivot = partition_using_right_most(
            array, low, high
        )  # Selecting the pivot element
        quick_sort_using_righmost_element(
            array, low, pivot - 1
        )  # Recursive method to sort left half
        quick_sort_using_righmost_element(
            array, pivot + 1, high
        )  # Recursive method to sort right half


# Implementing partition
def partition_using_right_most(array, low, high):
    # partition_using_right_most the right element as partition
    pivot = array[high]
    i = low - 1

    for j in range(low, high):
        if array[j] < pivot:
            i += 1
            # swapping smaller with higher vale
            array[i], array[j] = array[j], array[i]

    # Putting the pivot element in the correct position
    array[i + 1], array[high] = array[high], array[i + 1]
    return i + 1


########### Quick Sort implementation using left most element as pivot #############
## Creating a method to implment quick sort
def quick_sort_using_leftmost_element(array, low, high):
    if low < high:
        pivot = partition_using_left_most(
            array, low, high
        )  # Selecting the pivot element
        quick_sort_using_leftmost_element(
            array, low, pivot - 1
        )  # Recursive method to sort left half
        quick_sort_using_leftmost_element(
            array, pivot + 1, high
        )  # Recursive method to sort right half


# Implementing partition
def partition_using_left_most(array, low, high):
    # partition_using_right_most the right element as partition
    pivot = array[low]
    i = low

    for j in range(low + 1, high + 1):
        if array[j] < pivot:
            i += 1
            # swapping smaller with higher vale
            array[i], array[j] = array[j], array[i]

    # Putting the pivot element in the correct position
    array[low], array[i] = array[i], array[low]
    return i

    ## Creating a method to implment quick sort


########### Quick Sort implementation using mid element as pivot #############
def quick_sort_using_mid_element(array, low, high):
    if low < high:
        pivot = partition_using_mid(array, low, high)  # Selecting the pivot element
        quick_sort_using_mid_element(
            array, low, pivot - 1
        )  # Recursive method to sort left half
        quick_sort_using_mid_element(
            array, pivot + 1, high
        )  # Recursive method to sort right half


# Implementing partition
def partition_using_mid(array, low, high):
    # partition_using_right_most the right element as partition
    mid = (low + high) // 2
    pivot = array[mid]
    array[mid], array[high] = array[high], array[mid]
    i = low - 1

    for j in range(low, high):
        if array[j] < pivot:
            i += 1
            # swapping smaller with higher vale
            array[i], array[j] = array[j], array[i]

    # Putting the pivot element in the correct position
    array[i + 1], array[high] = array[high], array[i + 1]
    return i + 1


# Use cases with different array lists
sortedArray = list(range(0, 500))  # Sorted array from 1 to 499
# Applying merge sort in the above arrays
print("")
print("*************** Quick Sort Implementation for sorted element **************")
print("")
print("Applying quick sort to array 1 which is sorted using right most element")
startTime = time.time()
quick_sort_using_righmost_element(sortedArray, 0, len(sortedArray) - 1)
endTime = time.time()
print("Start time for sort process", startTime)
print("End time for sort process", endTime)
print(f"Execution time: {endTime - startTime:.6f} seconds")
print("sorted element", sortedArray)

print("Applying quick sort to array 1 which is sorted using left most element")
print("")
sortedArray = list(range(0, 500))  # Sorted array from 1 to 499
startTime = time.time()
quick_sort_using_leftmost_element(sortedArray, 0, len(sortedArray) - 1)
endTime = time.time()
print("Start time for sort process", startTime)
print("End time for sort process", endTime)
print(f"Execution time: {endTime - startTime:.6f} seconds")
print("sorted element", sortedArray)

print("Applying quick sort to array 1 which is sorted using mid element")
print("")
sortedArray = list(range(0, 500))  # Sorted array from 1 to 499
startTime = time.time()
quick_sort_using_mid_element(sortedArray, 0, len(sortedArray) - 1)
endTime = time.time()
print("Start time for sort process", startTime)
print("End time for sort process", endTime)
print(f"Execution time: {endTime - startTime:.6f} seconds")
print("sorted element", sortedArray)

print("")
print(
    "*************** Quick Sort Implementation for reverse sort element **************"
)
print("")
print("Applying quick sort to array 2 which is reverse sorted using right most element")
reverseSortedArray = list(range(500, 0, -1))
startTime = time.time()
quick_sort_using_righmost_element(reverseSortedArray, 0, len(reverseSortedArray) - 1)
endTime = time.time()
print("Start time for sort process", startTime)
print("End time for sort process", endTime)
print(f"Execution time: {endTime - startTime:.6f} seconds")
print("sorted element", reverseSortedArray)

reverseSortedArray = list(range(500, 0, -1))
print("")
print("Applying quick sort to array 1 which is reverse sorted using left most element")
startTime = time.time()
quick_sort_using_leftmost_element(reverseSortedArray, 0, len(reverseSortedArray) - 1)
endTime = time.time()
print("Start time for sort process", startTime)
print("End time for sort process", endTime)
print(f"Execution time: {endTime - startTime:.6f} seconds")
print("sorted element", reverseSortedArray)

reverseSortedArray = list(range(500, 0, -1))
print("")
print("Applying quick sort to array 1 which is  reverse sorted using mid element")
startTime = time.time()
quick_sort_using_mid_element(reverseSortedArray, 0, len(reverseSortedArray) - 1)
endTime = time.time()
print("Start time for sort process", startTime)
print("End time for sort process", endTime)
print(f"Execution time: {endTime - startTime:.6f} seconds")
print("sorted element", reverseSortedArray)

print("")
print(
    "*************** Quick Sort Implementation for random sort element **************"
)
print("")
print("Applying quick sort to array 2 which is reverse sorted using right most element")
randomSortedArray = [
    random.randint(1, 500) for _ in range(500)
]  # Random array of size 500
startTime = time.time()
quick_sort_using_righmost_element(randomSortedArray, 0, len(randomSortedArray) - 1)
endTime = time.time()
print("Start time for sort process", startTime)
print("End time for sort process", endTime)
print(f"Execution time: {endTime - startTime:.6f} seconds")
print("sorted element", randomSortedArray)

randomSortedArray = [
    random.randint(1, 500) for _ in range(500)
]  # Random array of size 500
print("")
print("Applying quick sort to array 1 which is reverse sorted using left most element")
startTime = time.time()
quick_sort_using_leftmost_element(randomSortedArray, 0, len(randomSortedArray) - 1)
endTime = time.time()
print("Start time for sort process", startTime)
print("End time for sort process", endTime)
print(f"Execution time: {endTime - startTime:.6f} seconds")
print("sorted element", randomSortedArray)

randomSortedArray = [
    random.randint(1, 500) for _ in range(500)
]  # Random array of size 500
print("")
print("")
print("Applying quick sort to array 1 which is  reverse sorted using mid element")
startTime = time.time()
quick_sort_using_mid_element(randomSortedArray, 0, len(randomSortedArray) - 1)
endTime = time.time()
print("Start time for sort process", startTime)
print("End time for sort process", endTime)
print(f"Execution time: {endTime - startTime:.6f} seconds")
print("sorted element", randomSortedArray)
