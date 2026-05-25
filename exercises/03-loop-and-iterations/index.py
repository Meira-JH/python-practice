NAMES = ['joão', 'paulo', 'matheus', 'marcos', 'pedro']

AGES = [21, 32, 45, 42, 55]

i = 0
while i < len(NAMES):
    print(NAMES[i], AGES[i])
    i+=1

for name, age in zip(NAMES, AGES):
    print(f"{name}: {age}")

for name in reversed(NAMES):
    print(name)

for i in range(5):
    print(i)

for i, name in enumerate(NAMES):
    print(f"{i}, {name}")