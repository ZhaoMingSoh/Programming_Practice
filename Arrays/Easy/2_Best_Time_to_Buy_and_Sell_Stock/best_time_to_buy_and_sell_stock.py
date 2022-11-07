import math

def best_time_to_buy_and_sell_stock(l:list[int]) -> int:
    ptr_l = 0
    ptr_r = 1

    max_profit = -math.inf

    while ptr_r <= len(l)-1:
        if l[ptr_l] < l[ptr_r]:
            local_profit = l[ptr_r] - l[ptr_l]
            if local_profit > max_profit:
                max_profit = local_profit
        else:
            ptr_l = ptr_r
        ptr_r += 1

    if max_profit < 0:
        max_profit = 0

    return max_profit


if __name__ == "__main__":
    l = [7,1,5,3,6,4]
    l_2 = [7,6,4,3,1]
    max_profit = best_time_to_buy_and_sell_stock(l_2)
    print(max_profit)