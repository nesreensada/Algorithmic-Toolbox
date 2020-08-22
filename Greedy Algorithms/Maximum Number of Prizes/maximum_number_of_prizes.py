# python3


def compute_optimal_summands(n):
    assert 1 <= n <= 10 ** 9
    summands = []
    for i in range(1, n+1):
        n -= i
        # when what is left is less than i then add n to the i
        if n <= i:
            summands.append(n+i)
            break
        # once i finish value return i and
        elif n == 0:
            summands.append(i)
            break
        # append i always
        else:
            summands.append(i)

    return summands



if __name__ == '__main__':
    input_n = int(input())
    output_summands = compute_optimal_summands(input_n)
    print(len(output_summands))
    print(*output_summands)
