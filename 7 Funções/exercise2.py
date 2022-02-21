def bigger_number_of_list(list):
    bigger = (0, list[0])
    i = 1
    while i < len(list):
        pos, val = bigger
        if list[i] > val:
            bigger = (i, list[i])
        i += 1
    return bigger

print(bigger_number_of_list([49, 35, 10, 82]))
