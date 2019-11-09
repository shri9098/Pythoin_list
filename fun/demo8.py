def isAlphabet(s):
    if 'a' <= s <= 'z' or 'A' <= s <= 'Z':
        return True
    return False


def swap(a, b):
    return b, a


def tolist1(string):
    lst1 = []
    for i in string:
        lst1.append(i)
    return lst1


def toString(lst1):
    return ''.join(lst1)


def reverse(string):
    lst = tolist1(string)
    r = len(string) - 1
    l = 0
    while l < r:
        if not isAlphabet(lst[l]):
            l += 1
        elif not isAlphabet(lst[r]):
            r -= 1
        else:
            lst[l], lst[r] = swap(lst[l], lst[r])
            l += 1
            r -= 1
    return toString(lst)


string = 'ABC#DE%FGH&I@'
print("Input string: ", string)
string = reverse(string)
print("Output string: ", string)
