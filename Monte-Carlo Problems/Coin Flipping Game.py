from random import choice


def coin_comparison(result, coin_num_l, coin_num_m, coin_num_n):
    if result[0] == result[1] == result[2]:
        return False
    elif result[0] == result[1]:
        coin_num_l += -1
        coin_num_m += -1
        coin_num_n += 2
        return coin_num_l, coin_num_m, coin_num_n
    elif result[0] == result[2]:
        coin_num_l += -1
        coin_num_m += 2
        coin_num_n += -1
        return coin_num_l, coin_num_m, coin_num_n
    elif result[1] == result[2]:
        coin_num_l += 2
        coin_num_m += -1
        coin_num_n += -1
        return coin_num_l, coin_num_m, coin_num_n


coin_num_l = float(input("The coin number for player 1:"))
coin_num_m = float(input("The coin number for player m:"))
coin_num_n = float(input("The coin number for player n:"))

toss_num_total = 0
coin = ["head", "tails"]
for i in range(10 ** 6):
    toss_num = 0
    coin_num_l = 2
    coin_num_m = 3
    coin_num_n = 4
    while coin_num_n > 0 and coin_num_m > 0 and coin_num_l > 0:
        l_coin_type = choice(coin)
        m_coin_type = choice(coin)
        n_coin_type = choice(coin)
        coin_types = [l_coin_type, m_coin_type, n_coin_type]
        N = coin_comparison(coin_types, coin_num_l, coin_num_m, coin_num_n)
        if not N:
            toss_num += 1
        else:
            coin_num_l = N[0]
            coin_num_m = N[1]
            coin_num_n = N[2]
            toss_num += 1
    toss_num_total += toss_num

print(toss_num_total / 10 ** 6)
