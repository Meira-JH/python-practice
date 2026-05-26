NAMES = ['joão', 'paulo', 'matheus']

AGES = [21, 32, 45]

JOAO = NAMES[0]
PAULO = NAMES[1]

JOAO_PAULO = NAMES[:2]
PAULO_MATHEUS = NAMES[1:]
REVERSE = NAMES[::-1]
EVERY_OTHER = NAMES[::1]

print('names')
print(JOAO)
print(PAULO)
print(JOAO_PAULO)
print(PAULO_MATHEUS)
print(REVERSE)
print(EVERY_OTHER)

print('ages')

print(sum(AGES))
print(min(AGES))
print(max(AGES))