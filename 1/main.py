with open('input.txt', 'r') as f:
    values = f.readlines()

total = 0
for value in values:
    total = total + int(value)

print(total)

current_frequencey = 0
observed_frequencies = set()

lookingForDouble = True
while lookingForDouble:
    for value in values:
        if current_frequencey in observed_frequencies:
            print(current_frequencey)
            lookingForDouble = False
            break
        observed_frequencies.add(current_frequencey)
        current_frequencey += int(value)