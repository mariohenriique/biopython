from Bio.Seq import Seq
from Bio import SeqIO

arquivo = SeqIO.parse("sequence.fasta","fasta")

for sequencia in arquivo:
    dna = sequencia.seq

# Podemos utilizar, como dito anteriormente, para fazer o complemento e o reverso
dna_complemento = dna.complement()
dna_reverse = dna.reverse_complement()

# Podemos fazer também a tradução e transcrição
rna_mensageiro = dna.transcribe()

# Transcrição da fita complementar
rna_complementar = dna.reverse_complement().transcribe()

# Transcrição reversa
dna_transcrito = rna_mensageiro.back_transcribe()

print(rna_mensageiro)
print(dna_transcrito)