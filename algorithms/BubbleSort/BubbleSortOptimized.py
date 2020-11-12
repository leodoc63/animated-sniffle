nums = [9, 8, 7, 6, 5, 4, 3, 2, 1]

print("Pre-Sort: {0}".format(nums))

def swap(arr, index_1, index_2):
    temp = arr[index_1]
    arr[index_1] = arr[index_2]
    arr[index_2] = temp
    
def bubble_sort_unoptimized(arr):
    iteration_count = 0
    for el in arr:
        for index in range(len(arr) -1):
            iteration_count += 1
            if arr[index] > arr[index + 1]:
                swap(arr, index, index + 1)
                
    print("Pre-Optimized iteration count: {0}".format(iteration_count))

def bubble_sort(arr):
    iteration_count = 0
    for i in range(len(arr)):
        for idx in range(len(arr) - i - 1):
            iteration_count += 1
            if arr[idx] > arr[idx + 1]:
                arr[idx], arr[idx + 1] = arr[idx + 1], arr[idx]
                
    print("Post-Optimized iteration count: {0}".format(iteration_count))
    

bubble_sort_unoptimized(nums.copy())
bubble_sort(nums)

print("Post-Sort: {0}".format(nums))

