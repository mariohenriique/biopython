# Para baixar o Biopython utilizando pip
# pip install biopython

# importando o pacote Biopython
# import Bio

# Mudando tipo de string para Seq
from Bio.Seq import Seq

seq1 = Seq("AGCT")
seq2 = Seq('CGTA')

# Pode utilizar a sequência em minúsculo
seq3 = Seq("agtctcgat")

# O que foi feito abaixo pode ser feito tanto para proteínas como código genético
# Pegando o reverso da sequencia (o reverso da outra fita de dna porém no sentido 5'->3')
revseq1 = seq1.reverse_complement()
revseq2 = seq2.reverse_complement()
revseq3 = seq3.reverse_complement()

# Complemento da sequencia
comp_seq1 = seq1.complement()
comp_seq2 = seq2.complement()
comp_seq3 = seq3.complement()

# Concatenando sequências
seq = seq1+seq2+seq3

# Concatenando com contigs
contig = [seq1,seq2,seq3]
espacador = Seq('-'*6)
seqcontig = espacador.join(contig)
seqcontig_maiscula = seqcontig.upper()
seqcontig_minuscula = seqcontig.lower()

print(f'A sequência 1 é {seq1} o reverso é {revseq1} e o complemento é {comp_seq1}')
print(f'A sequência 2 é {seq2} o reverso é {revseq2} e o complemento é {comp_seq2}')
print(f'A sequência 3 é {seq3} o reverso é {revseq3} e o complemento é {comp_seq3}')