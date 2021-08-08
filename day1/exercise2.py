
def number_1():
    print("number 1")
    print(50 + 50)
    print(100 - 10)


def number_2():
    print("number 2")
    print(30 * 6)
    print(6 ^ 6)
    print(6 ** 6)
    print(6 + 6 + 6 + 6 + 6 + 6)


def number_3():
    print("Hello World")
    print("Hello World : 10")


def number_4(months):
    p = 800000
    r = 0.06 / 12
    monthly_payment = (p * r * (1 + r) ** months) / ((1 + r) ** months - 1)
    print(monthly_payment)


if __name__ == '__main__':
    # number_1()
    # number_2()
    # number_3()
    number_4(480)
