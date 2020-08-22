# python3


def max_pairwise_product_naive(numbers):
    assert len(numbers) >= 2
    assert all(0 <= x <= 2 * 10 ** 5 for x in numbers)

    product = 0

    for i in range(len(numbers)):
        for j in range(i + 1, len(numbers)):
            product = max(product, numbers[i] * numbers[j])

    return product


def max_pairwise_product(numbers):
    assert len(numbers) >= 2
    assert all(0 <= x <= 2 * 10 ** 5 for x in numbers)
    n = len(numbers)
    max_index1 = 0
    for index in range(0,n):
        if numbers[index] > numbers[max_index1]:
            max_index1 = index
    max_index2 = 1 if max_index1 == 0 else 0
    for idx in range(0,n):
        if( (idx != max_index1) and  (numbers[idx] > numbers[max_index2]) ):
            max_index2 = idx
    return numbers[max_index1] * numbers[max_index2]


if __name__ == '__main__':
    n = int(input())
    input_numbers = list(map(int, input().split()))
    assert len(input_numbers) == n
    print(max_pairwise_product(input_numbers))
