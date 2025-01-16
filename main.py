import numpy

fieldSize = [10, 10]

field = []
field_line = []
for i in range(fieldSize[0]): 
    for j in range(fieldSize[1]):
        field_line.append(0)
    field.append(field_line)


def printField():
    for row in field:   # Loop through each row
        for num in row:  # Loop through each element in the row
            print(num, end=" ")  # Print elements in the same row with a space
        print()  # Newline after each row





def generateMines():
    for i in range(fieldSize[0]):
        for j in range(fieldSize[1]):
            if numpy.random.randint(0, 5) == 1:
                field[i][j] = 9


generateMines()

print(field)
printField()
