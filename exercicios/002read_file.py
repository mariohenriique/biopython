# Lendo um arquivo
from Bio import SeqIO

# utiliza o parse e coloca o arquivo e o formato
seq = SeqIO.parse("sequence.fasta","fasta")

# seq é um objeto iterador então é necessário utilizar o loop for para obter as informações.
for sequencia in seq:
    seq_id = sequencia.id
    seq_description = sequencia.description
    seq_name = sequencia.name
    seq_fasta = sequencia.seq
    seq_repr = repr(seq_fasta)
    seq_tamanho = len(sequencia)

# Lendo um arquivo gbk
seqgbk = SeqIO.parse('sequence.gb','genbank')

# Os utilizados anterior podem ser utilizados aqui.
for sequencia in seqgbk:
    seq_gbk = sequencia.seq

# Os arquivos baixados representam o mesmo sequenciamento para um mesmo indivíduo
# Verificando se ambos possuem o mesmo conteúdo
if seq_gbk == seq_fasta:
    print("São as mesmas sequências")