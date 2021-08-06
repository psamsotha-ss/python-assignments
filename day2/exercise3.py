import string


def number_1():
    print("Hello World"[8])


def number_2():
    print("thinker"[2:5])


def number_3():
    print("Sammy"[2:])


def number_4():
    print(set('Mississippi'))


def number_5():
    inputs = [
        'Stars',
        'O, a kak Uwakov lil vo kawu kakao!',
        'Some men interpret nine memos']
    for phrase in inputs:
        cleaned = phrase.strip(string.punctuation).replace(",", "").replace(" ", "").lower()
        reverse = cleaned[::-1]
        if cleaned == reverse:
            print('Y', end=' ')
        else:
            print('N', end=' ')


if __name__ == '__main__':
    number_1()
    number_2()
    number_3()
    number_4()
    number_5()
