# with open('input.txt', 'r') as f:
#     data = f.readline()

def findReaction(data):
    for i in range(1, len(data)):
        char1 = ord(data[i-1])
        char2 = ord(data[i])
        if(abs(char1-char2) == 32):
            return (i-1, i)
    return None


# while(True):
#     reaction = findReaction(data)
#     if(reaction is None):
#         break
    
#     left = reaction[0]
#     right = reaction[1]

#     data = data[0:left] + data[right+1:]

# print('HELLO')
# print(data)
# print(len(data))

# PART 2

with open('part2.txt', 'r') as f:
    data = f.readline()

shortestLength = len(data)
for i in range(ord('A'), ord('z')):
    char_to_remove = chr(i)
    filtered_data = data.replace(char_to_remove.lower(), "")
    filtered_data = filtered_data.replace(char_to_remove.upper(), "")

    while(True):
        reaction = findReaction(filtered_data)
        if(reaction is None):
            break
        
        left = reaction[0]
        right = reaction[1]

        filtered_data = filtered_data[0:left] + filtered_data[right+1:]

    if(len(filtered_data) < shortestLength):
        shortestLength = len(filtered_data)

print(shortestLength)