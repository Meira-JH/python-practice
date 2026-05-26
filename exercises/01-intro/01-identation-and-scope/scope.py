greet = 'hello world'

extend_greet = greet + ' this is an extended greeting'

name = 'João'

interruption = f"hello {name}"

greet_format = 'Hello {}'

formatted = greet_format.format(name)

print(greet)

print(extend_greet)

print(interruption, formatted)

print(formatted.upper())
print(formatted.lower())
print(formatted.replace('João', 'Paulo'))