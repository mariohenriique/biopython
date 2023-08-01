# Lendo um arquivo
from Bio import SeqIO

# utiliza o parse e coloca o arquivo e o formato
seq = SeqIO.parse("sequence.fasta","fasta")

# seq é um objeto iterador então é necessário utilizar o loop for para obter as informações.
for sequencia in seq:
    seq_id = sequencia.id
    seq_description = sequencia.description
    seq_name = sequencia.name
    seq_seq = sequencia.seq
    seq_repr = repr(seq_seq)
    seq_tamanho = len(sequencia)

# Lendo um arquivo gbk
seqgbk = SeqIO.parse('sequence.gb','genbank')

# Os utilizados anterior podem ser utilizados aqui.
for sequencia in seqgbk:
    print(sequencia)