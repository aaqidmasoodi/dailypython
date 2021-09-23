message = "Hello World"

print(type(message))
# String method
print(message.upper()) # need to change an input in uppercase
print(message.lower())
print(message.count('l'))

# apple # Apple # aPPle # applE # APPle
# commonly used validation technique
# it returns a new string and does not manuplate the old one

message = message.replace('World', 'Dayim') # commonly used pattern
message = "Hi kamran"
print(message)
