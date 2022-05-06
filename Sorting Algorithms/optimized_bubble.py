# Implementation of optimized bubble sort
# Time complexity is O(n)

def bubble_opt(element):
    size = len(element)

    # first number will automatically come to the right position.
    for i in range(size - 1):  # basically n-1 iteration should be done, for all passes.
        # set a variable swapped to false, because in the beginning nothing will be sorted.
        swapped = False
        for j in range(size - 1 - i):  # leaves the elements that are already sorted.
            if element[j] > element[j+1]:
                temp = element[j]
                element[j] = element[j+1]
                element[j+1] = temp
                swapped = True  # set swapped to true, when we are swapping

        # if we are not swapping after the end of the list
        # then we break, so that it takes less iteration
        # which is a result for best time complexity.
        # whereas in normal bubble sort we have to go through n-1 iteration
        # but in optimized bubble, the iteration will not happen if no need of sorting
        # so swapped working as a flag here.
        if not swapped:
            break


if __name__ == "__main__":
    elements = [5, 2, 1, 9, 67, 34, 88, 33]

    bubble_opt(elements)
    print(elements)

