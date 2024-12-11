# Open the file
file = open('/home/marcos/Repos/adventOfCode/01/test.txt', 'r')

# Initialize variables
data = []
amountLines = 0

# Read file line by line using a while loop
line = file.readline()
while line:
    # Split the line by whitespace and convert to integers
    data.append(list(map(int, line.split())))
    amountLines += 1
    # Read the next line
    line = file.readline()

# Close the file
file.close()

# Print the number of lines
print(amountLines)

i = 0
j = 0
left = [0] * amountLines
right = [0] * amountLines

while i < amountLines:
    left[i] = data[i][0]
    i += 1
left.sort()
i = 0

while i < amountLines:
    right[i] = data[i][1]
    i += 1
right.sort()

i = 0
distance = 0
while i < amountLines:
    distance = distance + abs((right[i]) - abs(left[i]))
    i += 1
print(distance)

i = 0
j = 0
count = 0
similarity = 0
while i < amountLines:
    count = 0
    j = 0
    while j < amountLines:
        if left[i] == right[j]:
            count += 1
        j+=1
        similarity = similarity + (left[i] * count)
        count = 0
    i+=1

print(similarity)

print(left)

