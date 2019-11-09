n = [0, 0, 1, 0, 00, 000, 1, 1, 1, 1]
new_num = []
while n:
    min = n[0]
    for x in n:
        if x < min:
            min = x
    new_num.append(min)
    n.remove(min)

print(new_num)