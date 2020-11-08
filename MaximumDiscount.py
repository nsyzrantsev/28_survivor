# https://github.com/nick-syz/skillsmart/blob/master/TankRush.py

def MaximumDiscount(N, price):
    res = ''
    price.sort(reverse=True)
    method1 = sum(price[-1:-int(N/3)])
    method2 = 0
    count = 2
    for i in range(int(N/3)):
        method2 += price[count]
        count += 3
    if method1 < method2:
        return method2
    return method1
