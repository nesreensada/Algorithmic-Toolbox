# python3

from itertools import permutations


def largest_number_naive(numbers):
    numbers = list(map(str, numbers))

    largest = 0

    for permutation in permutations(numbers):
        largest = max(largest, int("".join(permutation)))

    return largest
def isGreaterthenEqual(num1, num2):
    """
    This function checks if the first number
    :param num1:
    :param num2:
    :return: boolean if the first is bigger than the second one
    """
    # get the last digit for each number
    number1 = num1[0]
    number2 = num2[0]
    if number1 == number2:
        # check the bigest combination
        number1 = str(num1)+str(num2)
        number2 = str(num2) + str(num1)
    return number1 > number2
def largest_number(numbers):
    largest = ''
    numbers_copy = numbers.copy()
    while len(numbers_copy) > 0:
        max_digit = -1
        for digit in numbers_copy:
            if isGreaterthenEqual(str(digit), str(max_digit)):
                max_digit = digit
        largest += str(max_digit)
        numbers_copy.remove(max_digit)
    return int(largest)


if __name__ == '__main__':
    n = int(input())
    input_numbers = input().split()
    assert len(input_numbers) == n
    print(largest_number(input_numbers))
