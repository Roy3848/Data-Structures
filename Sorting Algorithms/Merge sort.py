# Implementation of Merge Sort

# defining the function to do merge sort
# and this function is to divide the array
def merge_sort(arr):
    # length of array is less than 1
    if len(arr) <= 1:
        return

    # divide the array into half
    mid = len(arr)//2

    # left array is start to the middle element of the array
    # right array is middle to the last element of the array.
    left = arr[:mid]
    right = arr[mid:]

    # merge both the half lists on the right and left
    merge_sort(left)
    merge_sort(right)

    merge_two_sorted_lists(left, right, arr)

# this function is to merge the arrays
def merge_two_sorted_lists(a,b,arr):
    len_a = len(a)
    len_b = len(b)

    i = j = k = 0

    # step by step merging based on the two halves.
    # as the array is broken till there is no way to further divide.
    # and once the array of both the halves are sorted then
    # after that, we are sorting the elements of different arrays
    while i < len_a and j < len_b:
        if a[i] <= b[j]:
            arr[k] = a[i]
            i+=1
        else:
            arr[k] = b[j]
            j+=1
        k+=1

    while i < len_a:
        arr[k] = a[i]
        i+=1
        k+=1

    while j < len_b:
        arr[k] = b[j]
        j+=1
        k+=1


# Driver Code
# Calling out the function
if __name__ == '__main__':
    elements = [11, 9, 29, 7, 2, 15, 28]
    merge_sort(elements)
    print(elements)
