# Implementation of selection sort

# defining the function for the selection sort
def selection_sort(arr):
    # length of the elements
    size = len(arr)
    for i in range(size - 1):
        min_index = i  # setting minimum index to i (minimum index from the unsorted array)
        for j in range(min_index+1, size):  # sorting through the unsorted array
            # if the element from the unsorted array is less than the
            # sorted array element then swap them
            if arr[j] < arr[min_index]:
                min_index = j
        # this is to swap the values.
        if i != min_index:
            arr[i], arr[min_index] = arr[min_index], arr[i]


if __name__ == "__main__":
    elements = [78, 12, 15, 8, 61, 53, 23, 27]
    selection_sort(elements)
    print(elements)
