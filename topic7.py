#Topic 7: Quick Sort for Priority Sorting
def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[0]
    left = [x for x in arr[1:] if x <= pivot]
    right = [x for x in arr[1:] if x > pivot]
    return quick_sort(left) + [pivot] + quick_sort(right)


data = [5, 3, 8, 1, 2, 9, 10, 18]
sorted_data = quick_sort(data)
print(sorted_data)  
