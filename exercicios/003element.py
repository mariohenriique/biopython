from Bio import SeqIO

seq = SeqIO.parse("sequence.fasta","fasta")

for i in seq:
    seq = i.seq

# Podemos acessar cada elemento da sequencia
base1 = seq[0]
base2 = seq[1]
base3 = seq[2]
baseultima = seq[-1]

# Contando os elementos da sequencia
# Podemos contar por exemplo quantas vezes um determinado códon aparece nessa sequência
codonTTT = seq.count('TTT')

# Conteúdo GC da sequência
# existem duas maneiras de fazer uma snao utilizando a biblioteca 
baseG = seq.count('G')
baseC = seq.count('C')
conteudo_GC = (baseG+baseC)/len(seq)*100

# Utilizando a biblioteca do biopython
from Bio.SeqUtils import gc_fraction
conteudo_GC_biblio = gc_fraction(seq)

# Selecionando uma parte da sequencia (semelhante a uma string ou um lista em pytohn)
# Elementos da 5° posição até a 11°
seq[4:12]

# Última bas4e do códon
seq[0::3]

# Sequência de trás para frente
seq[::-1]