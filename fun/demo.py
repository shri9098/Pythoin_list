def repeated_nu(l):
    size = len(l)
    repeat = []
    print(l)
    print(size, "size")
    for i in range(size):
        k = i + 1
        for j in range(k, size):
            if l[i] == l[j] and l[i] not in repeat:
                repeat.append(l[i])
    return repeat


lst = [1, 2, 3, 3, 4, 4, 5, 6, 7, 8, 9, 8, 1, 10]
print(repeated_nu(lst))

# def f(x, l=[]):
#     for i in range(x):
#         l.append(i * i)
#     print(l)
#
#
# f(2)
# f(3, [3, 2, 1])
# f(3)
#
#
# def check(s):
#     p = reversed(s)
#     print(p)
#
#
# s = 'sathya'
# check(s)
