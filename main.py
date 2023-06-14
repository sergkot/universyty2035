s = 'aabcca'


def strcount1(s):
    print('Hello)
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