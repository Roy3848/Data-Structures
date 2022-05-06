# Implementation of Bubble sort.

# defining a function
def bubble_sort(element):
    size = len(element)  # mentioning the length of the elements and size a variable

    # first number will automatically come to the right position.
    # that is the reason n-1 iteration
    for i in range(size - 1):  # this for loop basically for the passes. (Iteration)
        # To compare between the elements of the list
        # - i means leave the elements which are already sorted.
        for j in range(size - 1 - i):
            if element[j] > element[j+1]:
                temp = element[j]  # setting a variable temp to the element of index j.
                element[j] = element[j+1]
                element[j+1] = temp  # and finally swapping of the elements.


# Driver Code (calling out the function.)
if __name__ == "__main__":
    elements = [5, 2, 1, 9, 67, 34, 88, 33]

    bubble_sort(elements)
    print(elements)

