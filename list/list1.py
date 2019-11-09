def find_even_value_index(n):
    new_lst = []
    even_lst = []
    for x in range(0, n+1):
        if x % 2 == 0:
            new_lst.append(x)
    for i in range(0, len(new_lst)):
        if i % 2 == 0:
            even_lst.append(new_lst[i])

    print(new_lst, 'mod list')
    print(even_lst, "f_list")


n = input("enter any number :-")
find_even_value_index(int(n))
