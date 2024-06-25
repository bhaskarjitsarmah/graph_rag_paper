import os
import pandas as pd

def combine_csv_files_with_filenames(directory, output_file):
    # List to hold dataframes
    dataframes = []
    
    # Loop through all files in the directory
    for filename in os.listdir(directory):
        # Check if the file is a CSV
        if filename.endswith('.csv'):
            # Read the CSV file
            filepath = os.path.join(directory, filename)
            df = pd.read_csv(filepath)
            
            # Add a new column with the filename
            df['filename'] = filename
            
            # Append the dataframe to the list
            dataframes.append(df)
    
    # Concatenate all dataframes
    combined_df = pd.concat(dataframes, ignore_index=True)
    
    # Write the combined dataframe to a new CSV file
    combined_df.to_csv(output_file, index=False)

# Combine the CSV files

# Specify the directory containing the CSV files and the output file name
directory = 'D:\earning_call_eval\eval_out'
output_file = 'D:\earning_call_eval\evaluation_results.csv'

combine_csv_files_with_filenames(directory, output_file)