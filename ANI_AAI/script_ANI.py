with open('PneumoVSPyo_CDS_sorted.txt', 'r') as agaFile:
    agaLines = agaFile.readlines()

with open('/home/pl/Bureau/GECO-data/Strepto_Pyogenes/GCF_000006785.2_ASM678v2_feature_table.txt', 'r') as pyoFT:
    pyoFTLines = pyoFT.readlines()

with open('/home/pl/Bureau/GECO-data/Strepto_Pneumo/GCF_024089335.1_ASM2408933v1_feature_table.txt', 'r') as otherSpe:
    otherSpeLines = otherSpe.readlines()


def taking_the_cds(allLines):
    toSend_wp = {}
    toSend_spy = {}
    for line in allLines:
        dispatchElement = line.split("\t")
        if dispatchElement[0] == "CDS":
            if dispatchElement[10] == "":
                toSend_spy[dispatchElement[16]] = dispatchElement[17]
            else:
                toSend_wp[dispatchElement[10]] = dispatchElement[17]
    
    return toSend_wp, toSend_spy

specie_1_wp, specie_1_spy = taking_the_cds(pyoFTLines)
specie_2_wp, specie_2_spy = taking_the_cds(otherSpeLines)

# with open('LactisVSPyo_CDS_sorted.txt', 'r') as lacFile:
#     lacFile = lacFile.readlines()

# with open('PenanVSPyo_CDS_sorted.txt', 'r') as penanFile:
#     penanLines = penanFile.readlines()

# with open('PneumoVSPyo_CDS_sorted.txt', 'r') as pneuFile:
#     pneuFile = pneuFile.readlines()

# Query ID, Target ID, % id, lenght, mismatch...

count = 0
all_of_product = {}
list_of_lenght = []

# NC_004116.1_cds_WP_000312381.1_1451

for line in agaLines:
    if line != "\n":
        line_splitted = line.split('\t')
        id_one = "_".join(line_splitted[0].split("_")[3:5])
        if id_one not in specie_1_spy.keys() and  id_one not in specie_2_spy.keys():
            if id_one not in specie_1_wp.keys():
                list_of_lenght.append(int(specie_2_wp[id_one]))
            else:
                list_of_lenght.append(int(specie_1_wp[id_one]))
        else:
            if id_one not in specie_1_spy.keys():
                list_of_lenght.append(int(specie_2_spy[id_one]))
            else:
                list_of_lenght.append(int(specie_1_spy[id_one]))
        all_of_product[f"{line_splitted[0]} - {line_splitted[1]}"] = float(line_splitted[2]) * int(line_splitted[3])

final_result = sum(value for value in all_of_product.values())/sum(value for value in list_of_lenght)

print(final_result)