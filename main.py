s = 'aabcca'


def strcount1(s):
    print('Hello')
    for sym in set(s):
        # print(sym)
        counter = 0
        for sub_sym in s:
            if sub_sym == sym:
                counter += 1
        print(f'{sym} - {counter}')


strcount1(s)
print(set(s))


def strcounter(s):
    syms_counter = {}
    for sym in s:
        syms_counter[sym] = syms_counter.get(sym, 0) + 1
    print(syms_counter)


strcounter(s)

def palindrom(s):
    # first_pos = 0
    end_pos = len(s)
    ItIsPalindrom = True
    for first_pos in range(0, int(len(s)/2)):
        end_pos -= 1
        if s[first_pos] != s[end_pos]:
            ItIsPalindrom = False
            break
    return ItIsPalindrom

def palindrom_1(s):
    first_pos = 0
    end_pos = len(s) - 1
    ItIsPalindrom = True
    while first_pos < end_pos:
        if s[first_pos] != s[end_pos]:
            ItIsPalindrom = False
            break
        first_pos += 1
        end_pos -= 1
    return ItIsPalindrom



strcount1(s)
print(set(s))
print(palindrom('лепсспел'))
print(palindrom('helloworld'))

print('---------------')
print(palindrom_1('лепсспел'))
print(palindrom_1('helloworld'))