import random
import functools


def number_1():
    nums = [x for x in range(1500, 2700) if x % 7 == 0 and x % 5 == 0]
    print(nums)


def number_2():
    def celsius_to_fahrenheit(c):
        return (c * 9/5) + 32

    def fahrenheit_to_celsius(f):
        return (f - 32) * 5/9

    c_temp = 60
    print(f"{c_temp}C = {celsius_to_fahrenheit(c_temp)}F")
    f_temp = 45
    print(f"{f_temp}F = {fahrenheit_to_celsius(f_temp):.3}C")


def number_3():
    num = random.randint(1, 9)
    while True:
        guess = input("Enter a guess: ").strip()
        val = int(guess)
        if val == num:
            print('Well guessed!')
            break
        print('Try again.')


def number_4_and_5():
    rows = 10
    for i in range(1, rows):
        if i <= 5:
            stars = i
        else:
            stars = rows - i
        for j in range(stars):
            print('*', end='')
        print()


def number_6():
    user_input = input("Enter a word: ")
    reverse = user_input[::-1]
    print(reverse)


def number_7():
    nums = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    evens = functools.reduce(lambda count, val: count + 1 if val % 2 == 0 else count, nums, 0)
    print(f"evens: {evens}")
    odds = functools.reduce(lambda count, val: count + 1 if val % 2 != 0 else count, nums, 0)
    print(f"odds: {odds}")


def number_8():
    data_list = [1452, 11.23, 1 + 2j, True, 'w3resource', (0, -1), [5, 12], {"class": 'V', "section": 'A'}]
    for item in data_list:
        print(f'val: {item}: type: {type(item)}')


def number_9():
    for num in range(6 + 1):
        if num == 3 or num == 6:
            continue
        print(num, end=' ')
    print()


if __name__ == '__main__':
    # number_1()
    # number_2()
    # number_3()
    # number_4_and_5()
    # number_6()
    # number_7()
    # number_8()
    number_9()
