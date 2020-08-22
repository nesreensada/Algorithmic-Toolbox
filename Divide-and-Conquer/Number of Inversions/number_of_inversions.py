# python3

from itertools import combinations


def compute_inversions_naive(a):
    number_of_inversions = 0
    for i, j in combinations(range(len(a)), 2):
        if a[i] > a[j]:
            number_of_inversions += 1
    return number_of_inversions

def merge(a, b, left, mid, right):
    i = left     # Starting index of left subarray
    j = mid + 1 # Starting index of right subarray
    k = left     # Starting index of to be sorted subarray
    inv_count = 0
    while i <= mid - 1 and j <= right:
         # There will be no inversion if arr[i] <= arr[j]
        if a[i] <= a[j]:
            b[k] = a[i]
            i += 1
        else:
            # Inversion will occur.
            b[k] = a[j]
            j += 1
            inv_count += (mid - i + 1)
        k += 1
    # Copy the remaining elements of left subarray into temporary array
    while i <= mid:
        b[k] = a[i]
        i += 1
        k += 1

    # Copy the remaining elements of right subarray into temporary array
    while j <= right:
        b[k] = a[j]
        j += 1
        k += 1
    # Copy the sorted subarray into Original array
    for i in range(left, right + 1):
        a[i] = b[i]
    return inv_count


def merge_sort(a, b, left, right):
    inv_count = 0
    if right > left:
        mid = (left + right) // 2
         # It will calculate inversion counts in the left subarray
        inv_count += merge_sort(a, b, left, mid)
         # It will calculate inversion counts in the right subarray
        inv_count += merge_sort(a, b, mid + 1, right)
        # It will merge two subarrays in a sorted subarray
        inv_count += merge(a, b, left, mid , right)
    return inv_count

def compute_inversions(a):
    n = len(a)
    b = n * [0]
    return merge_sort(a, b, 0, n - 1)


if __name__ == '__main__':
    input_n = int(input())
    elements = list(map(int, input().split()))
    assert len(elements) == input_n
    print(compute_inversions(elements))
