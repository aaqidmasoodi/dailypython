frequencies = []

for i in range(27):
    frequencies.append(0)



with open('message.txt', 'r') as f:

    letter = f.read(1)


    while len(letter) > 0:
        if 65 <= ord(letter) <= 91 or 97 <= ord(letter) <= 122: # character is an alphabet

            location = ord(letter.lower()) - 97

            frequencies[location] += 1
        letter = f.read(1)


print(frequencies)



