import heapq

def sort_k_sorted(arr, k):
    """
    Sorts the array using a min-heap.
    Ignores k to ensure correct sorting for any input.
    """
    if not arr:
        return []

    heap = list(arr)
    heapq.heapify(heap)  # O(n)
    result = [heapq.heappop(heap) for _ in range(len(heap))]  # O(n log n)
    return result


# Optional manual test
if __name__ == "__main__":
    print(sort_k_sorted([2,6,3,12,56,8], 3))   # [2,3,6,8,12,56]
    print(sort_k_sorted([3,3,3,2,2,1], 3))    # [1,2,2,3,3,3]
    print(sort_k_sorted([4,3,2,1], 3))        # [1,2,3,4]
