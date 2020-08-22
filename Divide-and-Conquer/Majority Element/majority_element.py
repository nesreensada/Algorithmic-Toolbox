# python3


def majority_element_naive(elements):
    assert len(elements) <= 10 ** 5
    for e in elements:
        if elements.count(e) > len(elements) / 2:
            return 1

    return 0
# occurances of element in
def count_element(elements, x, left, right):
    count = 0
    for i in range(left, right):
        if elements[i] == x: count += 1
    return count

def _majority_element(elements, left, right):
    # last element
    if (right == left) or (right - left == 1):
        return elements[left]
    else:
        # split the tree
        mid = (left + right) // 2
        left_majority = _majority_element(elements, left, mid )
        right_majority = _majority_element(elements, mid + 1, right)
         # define whether there is a majority element for the part of the array
        # majority elements, exclude -1
        maj_elems = (a for a in (left_majority, right_majority) if a != -1)
        for element in maj_elems:
            if count_element(elements, element, left, right) > (right - left) / 2 :
                return 1
    return 0


def majority_element(elements):
    assert len(elements) <= 10 ** 5
    return majority_element_fast(elements)

def find_candidate(A):
    maj_index = 0
    count = 1
    for i in range(len(A)):
        if A[maj_index] == A[i]:
            count += 1
        else:
            count -= 1
        if count == 0:
            maj_index = i
            count = 1
    return A[maj_index]

def check_if_majority(A, cand):
    count = 0
    for i in range(len(A)):
        if A[i] == cand:
            count += 1
    if count > len(A)/ 2 : return 1
    else: return 0

def majority_element_fast(elements):
    candidate = find_candidate(elements)
    return check_if_majority(elements, candidate)

if __name__ == '__main__':
    input_n = int(input())
    input_elements = list(map(int, input().split()))
    assert len(input_elements) == input_n
    print(majority_element(input_elements))
