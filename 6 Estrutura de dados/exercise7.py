value = input('Digite algo: ')

times_appeared = {}

for character in value:
    try:
        quantity = times_appeared[character]+1
    except:
        quantity = 1
    times_appeared[character] = quantity

print(times_appeared)
