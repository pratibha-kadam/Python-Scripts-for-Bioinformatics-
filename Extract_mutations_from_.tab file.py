import sys

import pandas as pd
import os

# Define the directory path containing the .tab files
directory_path = r'D:/Cryptic_Variant_data/EE#74_CALLED_Copy'  # Replace 'your_directory_path' with the actual directory path

# Define a list of gene names to filter
selected_genes = ["Rv2535c","Rv0676c","Rv0677c","Rv0678","Rv1305","Rv1305"]  # Add more gene names as needed

# Create an empty DataFrame to store the results
result_df = pd.DataFrame(columns=['#Pos', 'Ref', 'Type', 'Allel', 'Subst', 'Gene', 'GeneName'])

# Create a dictionary to store filenames for each unique row data
row_data_to_filenames = {}

outs=[]
# Iterate through each file in the directory
for filename in os.listdir(directory_path):
    if filename.endswith(".tab"):  # Ensure you only process .tab files
        file_path = os.path.join(directory_path, filename)

        # Read the .tab file into a DataFrame
        df = pd.read_csv(file_path, sep='\t')
        df1 = df.filter(['#Pos', 'Ref', 'Type', 'Allel', 'Subst', 'Gene', 'GeneName'])

        # print(df1.columns)
        # print(df1)
        for value in selected_genes:
            # print(value)
            filtered_row = df1[df1['Gene'] == value]

            # Check if any rows match the value
            if not filtered_row.empty:
                # Print the row(s)
                # print(filtered_row.values.tolist(),filename)
                filtered_list=filtered_row.values.tolist()
                final_lst=[]
                for lp in filtered_list:
                    lp.append(filename)
                    # print(lp)
                    final_lst.append(lp)

                # outs=[]
                for i in range(len(final_lst)):
                    # print("--",final_lst[i])
                    for j in range(len(final_lst)):
                        # print(final_lst[i][:-1],final_lst[j][:-1])
                        # print(final_lst[i][:-1]==final_lst[j][:-1])
                        if final_lst[i][:-1]==final_lst[j][:-1]:
                            # print(final_lst[i][:-1],final_lst[j][-1])
                            # if final_lst[i] not in outs:
                            outs.append(final_lst[i])
                        #     print(final_lst[i],final_lst[-1])

            # filtered_df = pd.concat([df1, filtered_rows])
        # filtered_df.reset_index(drop=True, inplace=True)
        # print(filtered_df)
        # sys.exit()
        # Filter the DataFrame based on the 'Gene' column and selected gene names
        # filtered_data = df[df['Gene'].isin(selected_genes)]
        # filtered_data['FileName'] = os.path.basename(filename)
        #
        # # Iterate through rows in the filtered data
        # for index, row in filtered_data.iterrows():
        #     row_data = tuple(row.drop('FileName'))  # Exclude 'FileName' column for comparison
        #     if row_data in row_data_to_filenames:
        #         # Append the filename to the existing row data entry
        #         row_data_to_filenames[row_data].append(filename)
        #     else:
        #         # Create a new entry for the row data with a list of filenames
        #         row_data_to_filenames[row_data] = [filename]

# Iterate through the row data and
grouped_data = {}
print(outs)
for row in outs:
    values = tuple(row[:-1])  # Exclude the last element which is the file name
    file_name = row[-1]  # Get the file name
    if values in grouped_data:
        grouped_data[values].append(file_name)
    else:
        grouped_data[values] = [file_name]
    # if file_name in grouped_data:
    #     grouped_data[file_name].append(values)
    # else:
    #     grouped_data[file_name ] = [values]
# print(grouped_data)
# print(sys.exit())
# Find groups with multiple file names (same list of values)
duplicate_groups = {values: file_names for values, file_names in grouped_data.items() if
                    len(file_names) > 1}

f1=open("final_outs.csv","w")
# Print the groups with the corresponding file names
for values, file_names in duplicate_groups.items():
    print(f"{values} are present in the following .tab files: {', '.join(file_names)}",file=f1)
# print(filtered_list)
