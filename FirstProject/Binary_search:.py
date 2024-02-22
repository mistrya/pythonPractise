def binary_search(arr, target):
    """
    Perform binary search on a sorted array to find the target element.

    Parameters:
    - arr: A sorted list of elements.
    - target: The element to search for.

    Returns:
    - index: The index of the target element if found, else -1.
    """
    left = 0
    right = len(arr) - 1

    while left <= right:
        mid = (left + right) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1

    return -1


# Example usage:
arr = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19]
target = 11
result = binary_search(arr, target)
if result != -1:
    print(f"Element {target} is present at index {result}.")
else:
    print(f"Element {target} is not present in the array.")
