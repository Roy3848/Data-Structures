# Implementation of quick sort using python

# defining a function to do quick sort
def swap(a, b, arr):
    if a != b:
        # if a not equal to b is the condition
        # then call a variable tmp
        tmp = arr[a]
        arr[a] = arr[b]
        arr[b] = tmp

# defining a function to partition the array into two
# based on the pivot element we choose
# the partition is the pivot element
def quick_sort(elements, start, end):
    if start < end:
        pi = partition(elements, start, end)
        quick_sort(elements, start, pi-1)
        quick_sort(elements, pi+1, end)

# pivot element
def partition(elements, start, end):
    pivot_index = start
    pivot = elements[pivot_index]

    # all the elements that are less than pivot
    # will be on the left of the pivot element
    while start < end:
        while start < len(elements) and elements[start] <= pivot:
            start+=1

        # all the elements that are greater than the pivot
        # those elements are on the right side of the pivot element
        while elements[end] > pivot:
            end-=1

        if start < end:
            swap(start, end, elements)

    swap(pivot_index, end, elements)

    return end


# Driver Code
# calling out the function
if __name__ == '__main__':
    elements = [11,9,29,7,2,15,28]
    quick_sort(elements, 0, len(elements)-1)
    print(elements)

