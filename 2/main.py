def containsDuplicatesOfSameLetter(text, numberOfDuplicates):
    sorted_text = ''.join(sorted(text))
    current_letter = sorted_text[0]
    count = 0
    for letter in sorted_text:
        if current_letter != letter:
            current_letter = letter
            if count == numberOfDuplicates:
                return True
            count = 0
        count+=1

    if count == numberOfDuplicates:
        return True
    return False

with open('input.txt', 'r') as f:
    codes = f.readlines()

two_of_letter_count = 0
three_of_letter_count = 0

for code in codes:
    if containsDuplicatesOfSameLetter(code, 2):
        two_of_letter_count += 1
    if containsDuplicatesOfSameLetter(code, 3):
        three_of_letter_count += 1

print(two_of_letter_count)
print(three_of_letter_count)

print(two_of_letter_count * three_of_letter_count)



checksums = []
for code in codes:
    checksum = 0
    for index, letter in enumerate(code):
        checksum += ord(letter) * (index + 1) * (index + 1)
    checksums.append(checksum)

print(checksums)

checksums.sort()

for i in range(1, len(checksums)):
    if(checksums[i] - checksums[i-1] < 1):
        print(checksums[i])
        print('Hello')


#go through list and create a checksum
#sort in order
#find numbers that are close by

