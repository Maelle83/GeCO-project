file = "S-Pyogenes.txt"

file_content = open(file, 'r').readlines()

lst_result = []
for line in file_content:
    if line[0][0] != "#":
        if line.split("\t")[0] == "rRNA":
            lst_result.append(line.split("\t")[13])

print(len(lst_result))

rARN_diff = {}

for element in lst_result:
    if element not in rARN_diff:
        rARN_diff[element] = 1
    else:
        rARN_diff[element] += 1

print(rARN_diff)
