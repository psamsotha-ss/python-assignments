

def number_1():
    print('Hello World')


def number_2(name):
    print(f"Hello my name is {name}")


def number_3(x, y, z):
    if z:
        return x
    return y


def number_4(x, y):
    return x * y


def number_5(arg):
    def is_even(num):
        return num % 2 == 0
    print(is_even(arg))


def number_6(x, y):
    return x > y


def number_7(*args: int):
    total = 0
    for num in args:
        total += num
    print(total)
    return total


def number_8(*args: int):
    evens = []
    for arg in args:
        if arg % 2 == 0:
            evens.append(arg)
    print(evens)
    return evens


def number_9(string: str):
    index = 1
    result = ''
    for letter in string:
        if index % 2 == 1:
            result += letter.upper()
        else:
            result += letter.lower()
        index += 1
    print(result)
    return result


def number_10():
    """Don't understand question"""
    pass


def number_11(str1: str, str2: str):
    result = str1[0] == str2[0]
    print(result)
    return result


def number_12():
    """Don't understand question"""
    pass


def number_13(string: str):
    result = string[0].upper() + string[1:3] + string[3].upper() + string[4:]
    print(result)
    return result


if __name__ == '__main__':
    # number_1()
    # number_2('Google')
    # number_3(True, 1, 2)
    # number_4(2, 4)
    # number_5(10)
    # number_6(10, 20)
    # number_7(1, 2, 3, 4, 5)
    # number_8(1, 2, 3, 4, 5, 6)
    # number_9('HeLLO wOrld')
    # number_11('hello', 'world')
    number_13('hello world')
