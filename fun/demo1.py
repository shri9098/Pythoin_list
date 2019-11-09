# def f_list():
#     l = [1, 2, 4, 4, 6, 8, 8, 10]
#     _size = len(l)
#     l1 = []
#     l2 = []
#     for i in range(_size):
#         k = i + 1
#         for j in range(k, _size):
#             if l[i] == l[j] and l[i] not in l1:
#                 l1.append(l[i])
#
#     print(_size, "sasa")
#     for x in range(l[0], l[-1] + 1):
#         if x not in l:
#             l2 = x
#             print(l2)
#
#
# print(f_list())


def lst(l):
    size = len(l)
    print("size", size)
    l1 = []
    l2 = []
    for i in l:
        if i not in l1:
            l1.append(i)
    print(l1, 'repeated')
    for x in range(l[0], l[-1]+1):
        if x not in l:
            l2.append(x)
    print(l2, "missing")


l = [1, 2, 4, 4, 6, 8, 9, 8, 9, 10]
lst(l)
