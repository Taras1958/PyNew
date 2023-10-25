def palindrom(s):
    if len(s) <= 1:
        return True
    if s[0] != s[-1]:
        return False
    return palindrom(s[1:-1])
#
d = 'qweryrewq'
print(palindrom(d))

# s = 'кабак'

# # print(s[1:-1])
# print(d[1:-1])
