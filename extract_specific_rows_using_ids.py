import csv



# List of gene IDs you want to extract
desired_gene_ids = ["ENSG00000223972", "ENSG00000227232"]

# Input CSV file
input_csv_file = 'C:/Users/FMR/Desktop/python_pk/extact_specific_rows_from_csv/less_than_16.csv'

# Output CSV file to save the extracted rows
output_csv_file = "C:/Users/FMR/Desktop/python_pk/extact_specific_rows_from_csv/extracted_data.csv"

# Open the input and output files
with open(input_csv_file, 'r') as input_csv, open(output_csv_file, 'w', newline='') as output_csv:
    # Create CSV reader and writer objects
    csv_reader = csv.reader(input_csv)
    csv_writer = csv.writer(output_csv)

    # Read the header row and write it to the output file
    header = next(csv_reader)
    csv_writer.writerow(header)

    # Iterate through each row in the input CSV
    for row in csv_reader:
        gene_id = row[0]  # Assuming the gene ID is in the first column

        # Check if the gene ID is in the desired list
        if gene_id in desired_gene_ids:
            # If it's a desired gene ID, write the row to the output file
            csv_writer.writerow(row)

print(f"Rows for the desired gene IDs ({', '.join(desired_gene_ids)}) have been extracted to {output_csv_file}.")
