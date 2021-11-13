f = open('filename.txt', 'r')

contents = f.read()

for letter in contents:
    # TODO
    # ENCYRPT

f.close()


f = open('filename.txt', 'w')
f.write(generated_cipher_text)
f.close()


