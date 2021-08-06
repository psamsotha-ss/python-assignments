
def number_1():
    stuff = [100, 'hundred', 100.0]
    print(stuff)


def number_2():
    nums = [1, 1, [1, 2]]
    print(nums[2][1])


def number_3():
    lst = ['a', 'b', 'c']
    print(lst[1:])


def number_4(day):
    weekdays = {
        'SUNDAY': 1,
        'MONDAY': 2,
        'TUESDAY': 3,
        'WEDNESDAY': 4,
        'THURSDAY': 5,
        'FRIDAY': 6,
        'SATURDAY': 7}
    print(weekdays[day])


def number_5():
    d = {'k1': [1, 2, 3]}
    print(d['k1'][1])


def number_6():
    lst = [1, [2, 3]]
    print(tuple(lst))


def number_7():
    print(set('Mississippi'))


def number_8():
    letters = set('Mississippi')
    letters.add('X')
    print(letters)


def number_9():
    lst = [1, 1, 2, 3]
    print(set(lst))


def question_1():
    lst = [x for x in range(2000, 3200) if x % 7 == 0 and x % 5 != 0]
    print(lst)


def question_2(num):
    total = num
    while num > 1:
        num -= 1
        total *= num
    print(total)


def question_3(num):
    nums = {x: x*x for x in range(1, num + 1)}
    print(nums)


def question_4():
    nums = '1,2,3,4,5,6'
    print(list(nums.split(',')))
    print(tuple(nums.split(',')))


def question_5():
    class StringInput:
        def __init__(self):
            self.input = 'no input'

        def get_string(self):
            self.input = input('Enter string')

        def print_string(self):
            print(self.input.upper())


if __name__ == '__main__':
    number_1()
    number_2()
    number_3()
    number_4('MONDAY')
    number_5()
    number_6()
    number_7()
    number_8()
    number_9()
    question_1()
    question_2(8)
    question_3(8)
    question_4()
