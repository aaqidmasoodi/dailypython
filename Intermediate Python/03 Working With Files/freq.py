# write a python program to find the frequency of letters in a file

frequencies = {
        'a':0,'b':0,'c':0,'d':0,'e':0,'f':0,'g':0,'h':0,'i':0,'j':0,'k':0,'l':0,'m':0,
        'n':0,'o':0,'p':0,'q':0,'r':0,'s':0,'t':0,'u':0,'v':0,'w':0,'x':0,'y':0,'z':0,
    }


with open('message.txt', 'r') as f:

    letter = f.read(1)

    while letter:
        if letter.isalpha(): # character is an alphabet
            # TODO with letter
            frequencies[letter.lower()] += 1
        letter = f.read(1)


print(frequencies)

TOP FIVE FREQUENCY

