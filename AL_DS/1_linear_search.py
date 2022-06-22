# Start from the leftmost element of arr[] and one by one compare x with each element of arr[].
# Linear search is rarely used practically because other search algorithms such as the binary search algorithm and hash tables allow significantly faster-searching comparison to Linear search.

arr_data = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]

input = 10

def linear_search(arr, input):
    for i in range(0, len(arr)):
        if arr[i] == input:
            return i

    return -1        

result = linear_search(arr_data, input)

if result == -1:
    print("Element is not present in the array")
else:
    print("Element is present at index", result)

"""
def linear_search(arr, result):

    for index, value in enumerate(arr_data):
        if value == result:
            return index

    return -1   

result = linear_search(arr_data, input)

if(result == -1):
    print("Element is not present in the array")
else:
    print("Element is present at index", result) 
""" 

        
