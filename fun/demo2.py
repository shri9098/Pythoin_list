def missing_nu(l):
    missing_l = []
    return [x for x in range(l[0], l[-1]) if x not in missing_l]


l = [1, 2, 3, 4, 5, 8, 9, 101]
print(missing_nu(l))
