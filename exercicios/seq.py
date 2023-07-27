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

# Pegando o reverso da sequencia
revseq1 = seq1.reverse_complement()
revseq2 = seq2.reverse_complement()
revseq3 = seq3.reverse_complement()

# Complemento da sequencia
comp_seq1 = seq1.complement()
comp_seq2 = seq2.complement()
comp_seq3 = seq3.complement()

print(f'A sequência 1 é {seq1} o reverso é {revseq1} e o complemento é {comp_seq1}')
print(f'A sequência 2 é {seq2} o reverso é {revseq2} e o complemento é {comp_seq2}')
print(f'A sequência 3 é {seq3} o reverso é {revseq3} e o complemento é {comp_seq3}')