# python3


def fibonacci_number_again_naive(n, m):
    assert 0 <= n <= 10 ** 18 and 2 <= m <= 10 ** 3

    if n <= 1:
        return n

    previous, current = 0, 1
    for _ in range(n - 1):
        previous, current = current, (previous + current) % m

    return current

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
    assert 0 <= n <= 10 ** 18 and 2 <= m <= 10 ** 3
    assert 0 <= n <= 10 ** 18 and 2 <= m <= 10 ** 3
    period = pisano_period(m)
    # new n based on repeated period
    n = n % period
    res = n
    prev, curr = 0, 1
    for i in range(1, n):
        prev, curr = curr, (prev+curr) % m
        res = curr
    return (res % m )


if __name__ == '__main__':
    input_n, input_m = map(int, input().split())
    print(fibonacci_number_again(input_n, input_m))
