# Implementation of insertion sort

# Function to do insertion sort
def insertion_sort(arr):
    # Traverse through 1 to len(arr)
    for i in range(1, len(arr)):

        key = arr[i]

        # move elements of arr[0 to i-1],
        j = i - 1
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key


if __name__ == "__main__":
    elements = [11, 9, 29, 7, 2, 15, 28]
    insertion_sort(elements)
    print(elements)
