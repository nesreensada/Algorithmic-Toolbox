# python3


def last_digit_of_the_sum_of_squares_of_fibonacci_numbers_naive(n):
    assert 0 <= n <= 10 ** 18

    if n <= 1:
        return n

    fibonacci_numbers = [0] * (n + 1)
    fibonacci_numbers[0] = 0
    fibonacci_numbers[1] = 1
    for i in range(2, n + 1):
        fibonacci_numbers[i] = fibonacci_numbers[i - 2] + fibonacci_numbers[i - 1]

    return sum([f ** 2 for f in fibonacci_numbers]) % 10
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

def last_digit_of_the_sum_of_squares_of_fibonacci_numbers(n):
    assert 0 <= n <= 10 ** 18
    return (fibonacci_number_again(n,10) * fibonacci_number_again(n + 1, 10) )% 10


if __name__ == '__main__':
    input_n = int(input())
    print(last_digit_of_the_sum_of_squares_of_fibonacci_numbers(input_n))
