from pandas import read_csv


dict_of_aa = {}
RSCU_for_each_aa = {}


df = read_csv("Cusp_Penangensis", delim_whitespace=True)
for aa in df["AA"]:
    if aa not in dict_of_aa:
        dict_of_aa[aa] = 1
    else:
        dict_of_aa[aa] += 1

# Supposons que vous avez un dictionnaire `dict_of_aa` contenant les acides aminés en tant que clés
# et les nombres associés en tant que valeurs

with open("RSCU_Penangensis.txt", "w") as outFile:
    for key in dict_of_aa.keys():

        # Accédez à la valeur (nombre) correspondant à la clé (acide aminé) dans le dictionnaire
        valeur_associée = dict_of_aa[key]

        # Utilisez cette valeur pour filtrer le DataFrame
        # Filtrer les lignes pour l'acide aminé spécifique
        subset_df = df[df['AA'] == key]

        # Calculez la somme des valeurs dans la colonne 'Number' pour les autres codons ayant le même acide aminé
        somme_des_valeurs_autres_codons = subset_df['Number'].sum()

        # Parcourez chaque ligne du sous-DataFrame
        for index, row in subset_df.iterrows():
            codon = row['#Codon']
            number = row['Number']

            # Calculez le rapport du 'Number' par la somme des valeurs des autres codons
            rapport = round(
                number / (somme_des_valeurs_autres_codons/valeur_associée), 3)

            # Affichez le codon et le rapport
            outFile.write(f"{rapport}\n")

with open("Penangensis_frequency.txt", "w") as outFile:
    for line in df['Frequency']:
        outFile.write(f"{line}\n")
