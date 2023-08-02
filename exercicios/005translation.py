from Bio import SeqIO

arquivo = SeqIO.parse("sequence.gb","genbank")

for i in arquivo:
    sequencia = i.seq

rna_mensageiro = sequencia.transcribe()

# Para fazer a tradução a partir do rna mensageiro
proteina = rna_mensageiro.translate()

# Podemos utilizar outras tabelas de tradução do NCBI
proteina2 = rna_mensageiro.translate(table=2)

# Traduzinfo até o stop códon
proteina_stop = rna_mensageiro.translate(to_stop=True) # podemos utilizr também um símbolo para terminar a tradução (stop_symbol='símbolo')



print(proteina,proteina2)