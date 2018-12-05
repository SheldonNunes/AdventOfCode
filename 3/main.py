with open('input.txt', 'r') as f:
    claims = f.readlines()

fabric_size = 1000
matrix = [[0 for i in range(fabric_size)] for i in range(fabric_size)]

print(claims[0].split()[2].split(','))

for claim in claims:
    claim_split = claim.split(' ')

    coordinates = claim_split[2].split(',')
    x = int(coordinates[0])
    y = int(coordinates[1][0:-1])

    size = claim_split[3].split('x')
    width = int(size[0])
    height = int(size[1])
    for i in range(width):
        for j in range(height):
            matrix[x + i][y + j] += 1

result = 0
for row in matrix:
    result += sum(1 for c in row if c > 1)

print(result)

# Part 2

for claim in claims:
    claim_split = claim.split(' ')

    coordinates = claim_split[2].split(',')
    x = int(coordinates[0])
    y = int(coordinates[1][0:-1])

    size = claim_split[3].split('x')
    width = int(size[0])
    height = int(size[1])

    overlaps = False
    for i in range(width):
        for j in range(height):
            if matrix[x + i][y + j] > 1:
                overlaps = True
                break
    if overlaps is False:
        print(claim)