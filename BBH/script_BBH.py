entryInFileOne = {}
entryInFileTwo = {}

counter = 0

with open('test1', 'r') as fileOne:
    allLinesOne = fileOne.readlines()

counter = 0

with open('test2', 'r') as fileTwo:
    allLinesTwo = fileTwo.readlines()

for line in allLinesOne:
    entryInFileOne[allLinesOne.index(line)] = (line.split('\t')[0], line.split('\t')[1])

for line in allLinesTwo:
    entryInFileTwo[allLinesTwo.index(line)] = (line.split('\t')[1], line.split('\t')[0])


counter = 0

with open('___VSPyo.txt', 'w') as outFile:
    for index, value in entryInFileOne.items():
        if value in entryInFileTwo.values():
            index_in_file_two = list(entryInFileTwo.values()).index(value)
            outFile.write(f"{allLinesOne[index]}{allLinesTwo[index_in_file_two]}\n\n")
            counter += 1

print(counter)