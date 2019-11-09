def find_max():
    l = [1, 3, 5, 21, 7, 9, 11, 13]
    max = l[0]
    for x in l:
        if x > max:
            max = x
    print(max)


find_max()
