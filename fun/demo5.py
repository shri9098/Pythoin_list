data_list = [0, 0, 0, 0, 0, 0, 11, 111, 0, 0, 00, 0, 0, 1]
new_list = []

while data_list:
    minimum = data_list[0]  # arbitrary number in list
    for x in data_list:
        if x < minimum:
            minimum = x
    new_list.append(minimum)
    data_list.remove(minimum)

print(new_list)
