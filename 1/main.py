with open('input.txt', 'r') as f:
    values = f.readlines()

total = 0
for value in values:
    total = total + int(value)

print(total)