import heapq

def sort_k_sorted(arr, k):
    """
    Sorts a k-sorted array using a min-heap.
    :param arr: List[int] -- k-sorted array
    :param k: int -- maximum distance from sorted position
    :return: List[int] -- fully sorted array
    """
    if not arr or k == 0:
        return list(arr)  # already sorted or empty

    heap = arr[:k+1]  # first k+1 elements
    heapq.heapify(heap)

    result = []
    for i in range(k+1, len(arr)):
        # pop the smallest from heap and add to result
        result.append(heapq.heappop(heap))
        # push the next element from array
        heapq.heappush(heap, arr[i])

    # pop remaining elements from heap
    while heap:
        result.append(heapq.heappop(heap))

    return result


# Optional manual test
if __name__ == "__main__":
    print(sort_k_sorted([2,6,3,12,56,8], 3))  # [2,3,6,8,12,56]
