# Exercise 1

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




# Exercise 2


def containsOnlyOneDifference(box1, box2):
    count = 0
    for i in range(0, len(box1)):
        if(box1[i] != box2[i]):
            count += 1
            if count > 1:
                return False
    return True
        



for i in range(0, len(codes)):
    for j in range(i+1, len(codes)):
        result = containsOnlyOneDifference(codes[i], codes[j])
        if(result):
            print('Code 1:  ' + codes[i])
            print('Code 2:  ' + codes[j])

