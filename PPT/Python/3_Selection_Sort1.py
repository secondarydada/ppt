# Selection sort in Python
# Time complexity: O(n*n)
# Sorting by finding min_index

def selectionSort(array, size):
    for ind in range(size):
        min_index = ind

        for j in range(ind + 1, size):
            # Select the minimum element in every iteration
            if array[j] < array[min_index]:
                min_index = j

        # Swapping the elements to sort the array
        (array[ind], array[min_index]) = (array[min_index], array[ind])

# Taking user input for the array
arr = []
size = int(input("Enter the size of the array: "))
print("Enter the elements of the array:")
for i in range(size):
    element = int(input())
    arr.append(element)

# Calling the selectionSort function
selectionSort(arr, size)

# Printing the sorted array
print('The array after sorting in Ascending Order by selection sort is:')
print(arr)
