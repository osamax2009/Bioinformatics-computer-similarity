# from Bio import motifs 
# from Bio.Seq import Seq 
# DNA_motif = [ Seq("AGCT"), 
#               Seq("TCGA"), 
#                Seq("AACT"), 
#             ] 
# seq = motifs.create(DNA_motif) 
# print(seq)

# Open the file with sequences from Fernando de Noronha

from Bio import SeqIO
with open('data/mabuya_atlantica/noronha_mabuya.txt', 'r') as seq:
    noronha_file = SeqIO.parse(seq, 'fasta')
    noronha_sequences = [record for record in noronha_file]

