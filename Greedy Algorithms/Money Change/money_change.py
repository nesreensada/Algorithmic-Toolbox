# python3

def money_change(money):
    assert 0 <= money <= 10 ** 3
    count = 0
    remain = money
    for div in [10, 5, 1]:
        if remain == 0: return count
        if money // div != 0:
            count += remain // div
            remain = remain % div
    return count


if __name__ == '__main__':
    input_money = int(input())
    print(money_change(input_money))
