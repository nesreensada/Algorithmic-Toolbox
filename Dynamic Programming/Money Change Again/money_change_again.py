# python3


def change_naive(money):
    min_coins = float("inf")

    for num1 in range(money + 1):
        for num3 in range(money // 3 + 1):
            for num4 in range(money // 4 + 1):
                if 1 * num1 + 3 * num3 + 4 * num4 == money:
                    min_coins = min(min_coins, num1 + num3 + num4)

    return min_coins

def change_recursive(money):
    if money == 0:
        return 0
    min_coins = float("inf")
    coins = [1, 3, 4]
    for coin in coins:
        if money >= coin:
            num_coins = change(money - coin)
            if num_coins + 1 < min_coins:
                min_coins += num_coins
    return min_coins

def min_change(money, coins):
    for m in range(money):
        min_coins = float("inf")
        for coin in coins:
            if m >= coin:
                pass

def change(money):

    if money == 0:
        return 0
    #return min_change(money, [1, 3, 4])
    #coins = [0] * (money + 1)
    min_num_coins = [0] * (money + 1)
    for m in range(1, money + 1):
        min_num_coins[m] = float("inf")
        for coin in [1, 3, 4]:
            if m >= coin:
                num_coins = min_num_coins[m - coin] + 1
                if num_coins < min_num_coins[m]:
                    min_num_coins[m] = num_coins
    return min_num_coins[money]

        # if i < 3:
        #     coins[i] = i
        # elif i < 5:
        #     coins[i] = i
        # else:
        #     coins[i] = min(coins[i-1], coins[i-3], coins[i-4]) + 1
    #return coins[money]


if __name__ == '__main__':
    amount = int(input())
    print(change(amount))
