from Bio import SeqIO
input_file = open("extract_fasta/M_halo_VIT_protein.faa")
my_dict = SeqIO.to_dict(SeqIO.parse(input_file, "fasta"))
result_file="extract_fasta/Extracted_fasta.fasta"

#convert ids to list
with open("extract_fasta/core_VIT.txt") as f:
    ids = f.read().splitlines()

a= open(result_file, "w") #open file to write
for seq in my_dict:
        if seq in ids:
            print(">" + seq, '\n', my_dict[seq].seq,file=a)
a.close()






