# python3


def money_change(money):
    assert 0 <= money <= 10 ** 3
    count = 0
    while money > 0:
        if money >= 10:
            money -= 10
        elif money >= 5:
            money -= 5
        elif money >= 1:
            money -= 1
        count += 1
    return count


if __name__ == '__main__':
    input_money = int(input())
    print(money_change(input_money))
