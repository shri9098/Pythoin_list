def find_min():
    l = [11, 9, 3, 5, 0, 7, 13]
    min = l[0]
    for x in l:
        if x < min:
            min = x
    print(min)


find_min()
