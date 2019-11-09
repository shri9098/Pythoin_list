def repeated_chr(string):
    h = {}
    for ch in string:
        if ch in h:
            return ch
        else:
            h[ch]=0
    return 'None'


print(repeated_chr('sihri sri'))



