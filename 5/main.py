with open('input.txt', 'r') as f:
    data = f.readline()

def findReaction(data):
    for i in range(1, len(data)):
        char1 = ord(data[i-1])
        char2 = ord(data[i])
        if(abs(char1-char2) == 32):
            return (i-1, i)
    return None


while(True):
    reaction = findReaction(data)
    if(reaction is None):
        break
    
    left = reaction[0]
    right = reaction[1]

    data = data[0:left] + data[right+1:]

print('HELLO')
print(data)
print(len(data))