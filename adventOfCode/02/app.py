# Open the file in read mode
with open('/home/marcos/Repos/adventOfCode/02/test.txt', 'r') as file:
    # Read each line, strip any leading/trailing whitespace, and convert to a list of integers
    array_2d = [list(map(int, line.strip().split())) for line in file]

# Now `array_2d` contains the 2D array
print(array_2d)
print(array_2d[2][2])


