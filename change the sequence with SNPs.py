with open("MTB_genome.fna", 'r') as f:
    original_sequence = f.read()

def replace_bases_in_sequence(sequence, positions, new_bases):
    # Convert the sequence to uppercase to handle both cases
    sequence = sequence.upper()

    if len(positions) != len(new_bases):
        raise ValueError("Number of positions must match the number of new bases")

    for position in positions:
        if position < 1 or position > len(sequence):
            raise ValueError("Invalid position")

    for new_base in new_bases:
        if new_base not in ['A', 'T', 'C', 'G']:
            raise ValueError("Invalid new base")

    new_sequence = sequence

    for position, new_base in zip(positions, new_bases):
        # Convert position to 0-based index
        index = position - 1
        # Replace the base at the specified position
        new_sequence = new_sequence[:index] + new_base + new_sequence[index + 1:]

    return new_sequence

def main():
    fasta_header = ">NC_000962.3 Mycobacterium tuberculosis H37Rv, complete genome"
    

    original_Sequence = original_sequence
    positions_to_replace = [778994,779045,779052,779052,779109,779109,779107,779113,779125,779132,779138,779144,779165,779174,779186,779197,779236,779243,779268,779268,779275,779276,779308,779321,779350,779392,779405,779414,1461127,1461127,1461127,1461240,1461232,1461242,1461126,1461227,1461227,1461231,1461219,778991,779029,779048,779060,779062,779086,779096,779102,779108,779117,779120,779137,779141,779140,779147,779146,779159,779174,779176,779176,779188,779191,779192,779203,779204,779209,779210,779224,779225,779237,779240,779256,779269,779275,779285,779291,779293,779296,779312,779326,779330,779342,779351,779354,779363,779384,779392,779396,779406,779406,779406,779426,779440,779450
]
    new_bases = ['T','C','C','T','T','C','A','C','C','T','A','T','T','T','A','G','T','C','A','G','T','T','T','A','A','G','C','G','G','C','T','G','T','G','A','C','T','C','G','C','T','G','T','A','G','T','C','C','C','C','T','G','A','T','C','A','A','C','G','C','G','A','T','T','G','C','G','G','C','T','A','T','G','T','A','A','C','C','A','C','A','A','C','C','C','T','C','C','T','A','C','C','C']

    # Replace the bases at the specified positions with different bases
    replaced_sequence = replace_bases_in_sequence(original_sequence, positions_to_replace, new_bases)

    # Print the updated FASTA sequence
    output = print(f"{fasta_header}\n{replaced_sequence}")

   #with open('New_MTB_genome.txt', 'w') as file:
       # file.write(output)


if __name__ == "__main__":
    main()
