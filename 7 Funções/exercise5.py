def is_in_list(list, element):
    for value in list:
        if value == element:
            return True
    return False

print(is_in_list([1, 2, 3], 7))
