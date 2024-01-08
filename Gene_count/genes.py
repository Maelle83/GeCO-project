file = r'C:\Users\maell\OneDrive\Documents\Master2\TP_GECO\Floricoccus_penangensis\ncbi_dataset\data\GCF_001832885.1\genomic.gtf'  # Chemin du fichier gtf

with open(file, 'r') as gtf_file:
    total_length = 0
    num_gene = 0
    lengthlist = []

    for line in gtf_file:

        if line.startswith('#'):
            continue
        fields = line.strip().split('\t')
        feature_type = fields[0]
        if feature_type == 'gene':
            start = int(fields[3])
            end = int(fields[4])
            length = end - start + 1
            total_length += length
            num_gene += 1
            lengthlist.append(length)

moyenne = total_length / num_cds

print(f"Moyenne des longueurs des genes : {moyenne}")
print(f"max genes length: {max(lengthlist)}")
print(f"nb genes:{num_cds}")
print("Coding density")

# Faut modif la longueur du génome en pb selon l'organisme
print((total_length / 2049720) * 100)