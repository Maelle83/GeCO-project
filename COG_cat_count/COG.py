data = {
    'J': 'Translation, ribosomal structure and biogenesis',
    'A': 'RNA processing and modification',
    'K': 'Transcription',
    'L': 'Replication, recombination and repair',
    'B': 'Chromatin structure and dynamics',
    'D': 'Cell cycle control, cell division, chromosome partitioning',
    'Y': 'Nuclear structure',
    'V': 'Defense mechanisms',
    'T': 'Signal transduction mechanisms',
    'M': 'Cell wall/membrane/envelope biogenesis',
    'N': 'Cell motility',
    'Z': 'Cytoskeleton',
    'W': 'Extracellular structures',
    'U': 'Intracellular trafficking, secretion, and vesicular transport',
    'O': 'Posttranslational modification, protein turnover, chaperones',
    'X': 'Mobilome: prophages, transposons',
    'C': 'Energy production and conversion',
    'G': 'Carbohydrate transport and metabolism',
    'E': 'Amino acid transport and metabolism',
    'F': 'Nucleotide transport and metabolism',
    'H': 'Coenzyme transport and metabolism',
    'I': 'Lipid transport and metabolism',
    'P': 'Inorganic ion transport and metabolism',
    'Q': 'Secondary metabolites biosynthesis, transport and catabolism',
    'R': 'General function prediction only',
    'S': 'Function unknown'
}

file = "/home/pl/Téléchargements/EggNoggMap - S-Pyogenes.tsv"

file_content = open(file, 'r').readlines()

lst_result = []
for line in file_content:
    if line[0][0] != "#":
        if line.split("\t")[6] != "-":
            lst_result.append(line.split("\t")[6])


cog_cat = {}

for entry in lst_result:
    for char in entry:
        if char not in cog_cat:
            cog_cat[char] = 1
        else:
            cog_cat[char] += 1

print(len(lst_result))
print(cog_cat)
print("########################After correction#########################")
print(len(lst_result)-cog_cat['S'])

top_three = sorted(cog_cat.values(), reverse=True)[:4]

top_three_dic = {}

for key, value in cog_cat.items():
    for element in top_three:
        if value == element:
            if key != 'S':
                top_three_dic[key] = element

print(top_three_dic)
