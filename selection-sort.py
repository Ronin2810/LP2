'''The selection sort algorithm is often referred to as a "greedy" algorithm because it makes a locally optimal choice at each step with the hope that this will lead to a globally optimal solution.

In the case of selection sort, the algorithm greedily selects the smallest or largest element from the unsorted part of the array and swaps it with the element at the beginning of the unsorted part. By always choosing the smallest or largest element, depending on whether the sort is in ascending or descending order, the algorithm gradually builds up a sorted portion of the array.

However, it's important to note that selection sort is not a truly "greedy" algorithm in the traditional sense. In computer science, the term "greedy" typically refers to algorithms that make locally optimal choices at each step, without considering the global picture. In the case of selection sort, the algorithm is actually considering the entire unsorted portion of the array at each step, rather than making purely local choices.

Nonetheless, the term "greedy" has been associated with selection sort due to its incremental and locally optimal nature. It focuses on selecting the smallest or largest element at each step, making progress towards a sorted array.
'''



def selection_sort(arr):
    n = len(arr)

    for i in range(n):
        min_index = i
        for j in range(i + 1, n):
            if arr[j] < arr[min_index]:
                min_index = j

        arr[i], arr[min_index] = arr[min_index], arr[i]
        print("Array after iteration", i + 1, ":", arr)

    return arr

# Input from the user
input_str = input("Enter the elements of the array separated by space: ")
input_arr = [int(num) for num in input_str.split()]

# Display the array before sorting
print("Array before sorting:", input_arr)

# Sort the array using selection sort
sorted_arr = selection_sort(input_arr)

# Display the array after sorting
print("Array after sorting:", sorted_arr)
