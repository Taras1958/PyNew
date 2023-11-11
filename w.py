import string


def my_func(st):
    all_chars = string.ascii_lowercase + string.ascii_uppercase + string.digits + '_@.'
    for i in st:
        if i not in all_chars:
            print('НЕТ')
    print('ДА')

st1 = input()
my_func(st1)
