# python3


def last_digit_of_the_sum_of_fibonacci_numbers_again_naive(from_index, to_index):
    assert 0 <= from_index <= to_index <= 10 ** 18

    if to_index == 0:
        return 0

    fibonacci_numbers = [0] * (to_index + 1)
    fibonacci_numbers[0] = 0
    fibonacci_numbers[1] = 1
    for i in range(2, to_index + 1):
        fibonacci_numbers[i] = fibonacci_numbers[i - 2] + fibonacci_numbers[i - 1]

    return sum(fibonacci_numbers[from_index:to_index + 1]) % 10

def pisano_period(m):
    """
    This functions finds the pisano period for the a given m value
    :param m:
    :return: pisano period length
    """
    prev, curr = 0, 1
    # the pisano period range from 3 to m * m
    for i in range(0, m*m):
        prev, curr = curr, (prev+ curr) % m
        # we have reached the pattern again
        if (prev == 0 and curr == 1):
            return i+1

def fibonacci_number_again(n, m):
    """
    :param n:
    :param m:
    :return:
    the last digit of fib num
    """
    period = pisano_period(m)
    # new n based on repeated period
    n = n % period
    res = n
    prev, curr = 0, 1
    for i in range(1, n):
        prev, curr = curr, (prev+curr) % m
        res = curr
    return (res % m )



def last_digit_of_the_sum_of_fibonacci_numbers_again(from_index, to_index):
    assert 0 <= from_index <= to_index <= 10 ** 18

    return (fibonacci_number_again(to_index+2, 10) + 10 - fibonacci_number_again(from_index+1, 10)) % 10


if __name__ == '__main__':
    input_from, input_to = map(int, input().split())
    print(last_digit_of_the_sum_of_fibonacci_numbers_again(input_from, input_to))
