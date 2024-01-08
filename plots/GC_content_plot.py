
from Bio import SeqIO
import matplotlib.pyplot as plt

def calculate_gc_content(sequence, window_size):
    gc_content = []
    for i in range(0, len(sequence), window_size):
        window = sequence[i:i + window_size]
        gc_count = window.count('G') + window.count('C')
        gc_percent = (gc_count / len(window)) * 100
        gc_content.append(gc_percent)
    return gc_content

def main(fasta_files, window_size):
    for fasta_file in fasta_files:
        sequences = SeqIO.parse(fasta_file, 'fasta')
        for record in sequences:
            sequence = str(record.seq)
            gc_content = calculate_gc_content(sequence, window_size)
            position = list(range(0, len(sequence), window_size))
            plt.scatter(position, gc_content,marker='x' ,label=record.id)

    plt.xlabel('Position (base pairs)')
    plt.ylabel('GC Content (%)')
    plt.ylim(0, 100)
    plt.legend()
    plt.title('Compararison of GC content accross sequence in several organism')
    plt.grid(True)
    plt.show()

#Petite couille pour le Penangensis

if __name__ == "__main__":
    fasta_files = ['Pyogenes.fna', 'agalactiae.fna', 'lactis.fna', 'Pneumo.fna', 'Penangensis.fna']
    window_size = 100
    main(fasta_files, window_size)